import os
import stripe
from domain.entities.doacao import Doacao
from domain.ports.doacao_repository import DoacaoRepository


class DoacaoService:
    def __init__(self, repo: DoacaoRepository) -> None:
        self.repo = repo
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
        if dados.get("nome_projeto"):
            metadata["nome_projeto"] = dados["nome_projeto"]

        success_url = os.getenv("STRIPE_SUCCESS_URL", "http://localhost:8000/doacoes/sucesso")
        cancel_url = os.getenv("STRIPE_CANCEL_URL", "http://localhost:8000/doacoes/cancelado")

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

        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            self.repo.update_status(session["id"], "pago")
