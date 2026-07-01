"""Financeiro — doações externas, despesas e histórico de transparência."""
import streamlit as st

from api import make_request, error_detail
from ui import flash, show_flash


def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def financeiro_section():
    st.subheader("Financeiro")
    st.caption("Lance doações externas e despesas. Registros são permanentes e não podem ser editados.")

    show_flash()

    aba_opcoes = ["Lançar Doação Externa", "Lançar Despesa", "Histórico"]
    if "financeiro_aba_ativa" not in st.session_state:
        st.session_state["financeiro_aba_ativa"] = aba_opcoes[0]

    aba_selecionada = st.radio(
        "Seção financeira",
        aba_opcoes,
        horizontal=True,
        key="financeiro_aba_ativa",
        label_visibility="collapsed",
    )

    # doacao externa
    if aba_selecionada == "Lançar Doação Externa":
        with st.form("form_doacao", clear_on_submit=True):
            col1, col2 = st.columns(2)
            valor = col1.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f")
            data = col2.date_input("Data da doação")
            descricao = st.text_area("Descrição", placeholder="ex: Doação em dinheiro recebida no evento de Maio")

            if st.form_submit_button("Confirmar doação"):
                if not descricao:
                    st.error("Preencha a descrição.")
                else:
                    st.session_state["pending_doacao"] = {
                        "valor": valor,
                        "data": data.isoformat(),
                        "descricao": descricao,
                    }

        pending = st.session_state.get("pending_doacao")
        if pending:
            st.warning(
                f"Tem certeza que deseja registrar a doação de "
                f"**R$ {pending['valor']:,.2f}** — \"{pending['descricao']}\"?\n\n"
                "Essa ação não pode ser desfeita."
            )
            c1, c2 = st.columns(2)
            if c1.button("Sim, confirmar doação", type="primary", width='stretch', key="btn_confirma_doacao"):
                with st.spinner("Registrando doação..."):
                    resp = make_request("POST", "/transparencia/doacao-externa", data=pending)
                if resp is not None and resp.status_code == 200:
                    del st.session_state["pending_doacao"]
                    flash("Doação registrada com sucesso!")
                    st.rerun()
                elif resp is not None:
                    st.error(error_detail(resp))
            if c2.button("Cancelar", width='stretch', key="btn_cancela_doacao"):
                del st.session_state["pending_doacao"]
                st.rerun()

   # despesa
    if aba_selecionada == "Lançar Despesa":
        with st.form("form_despesa", clear_on_submit=True):
            col1, col2 = st.columns(2)
            valor = col1.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f", key="valor_despesa")
            data = col2.date_input("Data da despesa", key="data_despesa")
            categoria = st.text_input("Categoria", placeholder="ex: Aluguel, Material, Transporte")

            if st.form_submit_button("Confirmar despesa"):
                if not categoria:
                    st.error("Preencha a categoria.")
                else:
                    st.session_state["pending_despesa"] = {
                        "valor": valor,
                        "data": data.isoformat(),
                        "categoria": categoria,
                    }

        pending = st.session_state.get("pending_despesa")
        if pending:
            st.warning(
                f"Tem certeza que deseja registrar a despesa de "
                f"**R$ {pending['valor']:,.2f}** — \"{pending['categoria']}\"?\n\n"
                "Essa ação não pode ser desfeita."
            )
            c1, c2 = st.columns(2)
            if c1.button("Sim, confirmar despesa", type="primary", width='stretch', key="btn_confirma_despesa"):
                with st.spinner("Registrando despesa..."):
                    resp = make_request("POST", "/transparencia/despesa", data=pending)
                if resp is not None and resp.status_code == 200:
                    del st.session_state["pending_despesa"]
                    flash("Despesa registrada com sucesso!")
                    st.rerun()
                elif resp is not None:
                    st.error(error_detail(resp))
            if c2.button("Cancelar", width='stretch', key="btn_cancela_despesa"):
                del st.session_state["pending_despesa"]
                st.rerun()

    # historico
    if aba_selecionada == "Histórico":
        st.caption(
            "🟢 **Doação externa** — recurso recebido de fora da organização (pessoa física, empresa ou evento). "
            "🔵 **Doação interna** — recurso originado internamente por meio de doações realizadas dentro do aplicativo."
        )
        resp = make_request("GET", "/transparencia")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return

        records = resp.json()
        if not isinstance(records, list):
            st.error("Resposta inesperada do servidor")
            return
        if not records:
            st.info("Nenhum registro encontrado.")
            return

        total_in = sum(r["valor"] for r in records if r["tipo"] != "despesa")
        total_out = sum(r["valor"] for r in records if r["tipo"] == "despesa")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total arrecadado", formatar_real(total_in))
        c2.metric("Total de despesas", formatar_real(total_out))
        c3.metric("Saldo", formatar_real(total_in - total_out))

        st.divider()

        for r in records:
            render_transparencia_card(r)


def render_transparencia_card(r):
    tipo_meta = {
        "doacao_externa": ("Doação externa", "pill-vaga", "#16A34A"),
        "doacao_interna": ("Doação interna", "pill-post", "#2563EB"),
        "despesa":        ("Despesa",        "pill-despesa", "#E11D48"),
    }
    label, pill_cls, dot_color = tipo_meta.get(r["tipo"], ("Registro", "pill-inactive", "#94A3B8"))
    sinal = "-" if r["tipo"] == "despesa" else "+"
    cor_valor = "#E11D48" if r["tipo"] == "despesa" else "#16A34A"
    data_fmt = r["data"][:10] if r.get("data") else "—"

    with st.container(border=True):
        col_info, col_valor = st.columns([4, 1])
        with col_info:
            st.markdown(
                f'<span class="pill {pill_cls}">'
                f'<span class="dot" style="background:{dot_color};"></span>{label}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<div class="card-title">{r["descricao"]}</div>', unsafe_allow_html=True)
            if r.get("destino"):
                st.markdown(
                    f'<div class="card-meta">📍 {r["destino"]}</div>',
                    unsafe_allow_html=True,
                )
            st.markdown(f'<div class="card-meta">{data_fmt}</div>', unsafe_allow_html=True)
        with col_valor:
            st.markdown(
                f'<div style="text-align:right; font-weight:800; font-size:1.1rem; '
                f'color:{cor_valor}; padding-top:8px;">{sinal} {formatar_real(r["valor"])}</div>',
                unsafe_allow_html=True,
            )
