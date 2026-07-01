import os
from datetime import datetime, timezone

import stripe

from domain.entities.doacao import Doacao
from domain.entities.transparencia_record import TransparenciaRecord, TipoRegistro
from domain.ports.doacao_repository import DoacaoRepository


class DoacaoService:
    def __init__(self, repo: DoacaoRepository, worm_storage=None, transparencia_service=None) -> None:
        self.repo = repo
        self.worm_storage = worm_storage
        self.transparencia_service = transparencia_service
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def criar_checkout_session(self, dados: dict) -> str:
        valor: float = dados["valor"]
        is_anonima: bool = dados.get("is_anonima", False)
        direcao: str = dados.get("direcao", "instituicao")

        metadata = {
            "is_anonima": str(is_anonima),
            "direcao": direcao,
        }
        if dados.get("nome_doador"):
            metadata["nome_doador"] = dados["nome_doador"]
        if dados.get("cpf"):
            metadata["cpf"] = dados["cpf"]
        if dados.get("nome_projeto"):
            metadata["nome_projeto"] = dados["nome_projeto"]

        success_url = os.getenv("STRIPE_SUCCESS_URL", "http://localhost:8000/doacoes/sucesso")
        cancel_url = os.getenv("STRIPE_CANCEL_URL", "http://localhost:8000/doacoes/cancelado")

        # Anexa o id da sessão à URL de sucesso para permitir confirmar o
        # pagamento no redirect (essencial quando o webhook do Stripe não
        # alcança o backend, ex.: ambiente local sem Stripe CLI).
        sep = "&" if "?" in success_url else "?"
        success_url = f"{success_url}{sep}session_id={{CHECKOUT_SESSION_ID}}"

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "brl",
                    "product_data": {"name": "Doação DoaNet"},
                    "unit_amount": int(round(valor * 100)),
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
            metadata=metadata,
        )

        doacao = Doacao(
            valor=valor,
            is_anonima=is_anonima,
            nome_doador=dados.get("nome_doador"),
            cpf=dados.get("cpf"),
            endereco=dados.get("endereco"),
            direcao=direcao,
            nome_projeto=dados.get("nome_projeto"),
            stripe_session_id=session.id,
            status="pendente",
            checkout_url=session.url,
        )
        self.repo.save(doacao)

        return session.url

    def processar_webhook(self, payload: bytes, sig_header: str) -> None:
        webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        if event["type"] != "checkout.session.completed":
            return

        session = event["data"]["object"]
        session_id = session["id"] if isinstance(session, dict) else session.id
        self.confirmar_pagamento(session_id)

    def confirmar_pagamento(self, session_id: str) -> None:
        """Confirma uma doação paga. Idempotente: pode ser chamado tanto pelo
        webhook do Stripe quanto pelo redirect de sucesso sem duplicar
        registros."""
        if not session_id:
            return

        doacao = self.repo.find_by_session_id(session_id)

        # Idempotência: se a doação já foi confirmada, não reprocessa.
        if doacao is not None and doacao.status == "pago":
            return

        # Sem dependências estendidas: comportamento legado (apenas status).
        if self.worm_storage is None and self.transparencia_service is None:
            self.repo.update_status(session_id, "pago")
            return

        # Processamento completo. O status "pago" só é gravado ao final
        # (dentro de _registrar_doacao_confirmada), tornando a operação
        # segura para retry caso a gravação no WORM ou na transparência falhe.
        self._registrar_doacao_confirmada(session_id, doacao)

    # ------------------------------------------------------------------
    # Confirmação: coleta dados do Stripe, grava WORM e cria doação interna
    # ------------------------------------------------------------------
    def _registrar_doacao_confirmada(self, session_id: str, doacao=None) -> None:
        if doacao is None:
            doacao = self.repo.find_by_session_id(session_id)
        stripe_info = self._coletar_dados_stripe(session_id)

        # Campos extraídos do Stripe
        payment_status = stripe_info.get("payment_status")
        payment_method = stripe_info.get("payment_method")
        card_brand = stripe_info.get("card_brand")
        card_last4 = stripe_info.get("card_last4")
        moeda = stripe_info.get("currency")
        valor_total = stripe_info.get("amount_total")
        payment_intent_id = stripe_info.get("payment_intent_id")

        campos_stripe = {
            "status": "pago",
            "payment_status": payment_status,
            "payment_method": payment_method,
            "card_brand": card_brand,
            "card_last4": card_last4,
            "moeda": moeda,
            "valor_total": valor_total,
            "stripe_payment_intent_id": payment_intent_id,
            "stripe_info": stripe_info.get("raw"),
        }

        # Monta o registro imutável (WORM) com dados do formulário + Stripe
        worm_record = {
            "tipo": "doacao_interna",
            "registrado_em": datetime.now(timezone.utc).isoformat(),
            "doacao": doacao.model_dump() if doacao else {"stripe_session_id": session_id},
            "stripe": stripe_info,
        }

        # 1º) Grava o comprovante imutável no WORM storage.
        worm_path = None
        if self.worm_storage is not None:
            resultado = self.worm_storage.upload_json(worm_record, prefix="doacoes")
            worm_path = resultado.get("worm_path")
            campos_stripe["worm_path"] = worm_path

        # 2º) Cria o registro na aba de transparência como doação interna.
        if self.transparencia_service is not None:
            self._criar_registro_transparencia(doacao, valor_total)

        # 3º) Só então persiste os dados do Stripe e marca como "pago".
        # Como este é o último passo, uma falha anterior deixa a doação
        # como "pendente" e permite o reprocessamento em nova tentativa.
        self.repo.update_by_session_id(session_id, campos_stripe)

    def _criar_registro_transparencia(self, doacao, valor_total) -> None:
        valor = None
        is_anonima = True
        nome_doador = None
        direcao = None
        nome_projeto = None

        if doacao is not None:
            valor = doacao.valor
            is_anonima = doacao.is_anonima
            nome_doador = doacao.nome_doador
            direcao = doacao.direcao
            nome_projeto = doacao.nome_projeto

        if valor is None:
            valor = valor_total

        if is_anonima or not nome_doador:
            descricao = "Doação interna anônima"
        else:
            descricao = f"Doação interna de {nome_doador}"

        if direcao == "projeto" and nome_projeto:
            descricao += f" — Projeto: {nome_projeto}"

        record = TransparenciaRecord(
            tipo=TipoRegistro.DOACAO_INTERNA,
            valor=valor,
            data=datetime.now(timezone.utc),
            descricao=descricao,
            created_by="stripe-webhook",
        )
        self.transparencia_service.add_record(record)

    def _coletar_dados_stripe(self, session_id: str) -> dict:
        """Recupera do Stripe todos os dados possíveis sobre o pagamento."""
        info: dict = {}
        try:
            session = stripe.checkout.Session.retrieve(
                session_id,
                expand=["payment_intent", "payment_intent.payment_method", "line_items"],
            )
        except Exception as exc:
            info["erro"] = str(exc)
            return info

        info["session_id"] = session_id
        info["payment_status"] = self._get(session, "payment_status")
        amount_total = self._get(session, "amount_total")
        info["amount_total"] = amount_total / 100 if amount_total is not None else None
        info["currency"] = self._get(session, "currency")

        customer_details = self._get(session, "customer_details")
        if customer_details is not None:
            info["customer"] = self._para_dict(customer_details)

        payment_intent = self._get(session, "payment_intent")
        if payment_intent is not None:
            info["payment_intent_id"] = self._get(payment_intent, "id")
            info["payment_intent_status"] = self._get(payment_intent, "status")
            payment_method = self._get(payment_intent, "payment_method")
            if payment_method is not None:
                pm_type = self._get(payment_method, "type")
                info["payment_method"] = pm_type
                card = self._get(payment_method, "card")
                if card is not None:
                    info["card_brand"] = self._get(card, "brand")
                    info["card_last4"] = self._get(card, "last4")

        info["raw"] = self._para_dict(session)
        return info

    @staticmethod
    def _get(obj, key):
        if obj is None:
            return None
        if isinstance(obj, dict):
            return obj.get(key)
        return getattr(obj, key, None)

    @staticmethod
    def _para_dict(obj):
        if obj is None:
            return None
        if isinstance(obj, dict):
            return obj
        for metodo in ("to_dict_recursive", "to_dict"):
            fn = getattr(obj, metodo, None)
            if callable(fn):
                try:
                    return fn()
                except Exception:
                    continue
        try:
            return dict(obj)
        except Exception:
            return str(obj)
