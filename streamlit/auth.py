"""Autenticação: login e cadastro do administrador principal."""
import requests
import streamlit as st

from config import BACKEND_URL
from api import error_detail


def check_first_admin():
    try:
        response = requests.get(f"{BACKEND_URL}/admin/check-first", timeout=10)
        return response.json().get("has_admins", False)
    except requests.exceptions.RequestException:
        return None  # backend offline


_LOGIN_CSS = """
<style>
/* ---- Estilos exclusivos da tela de login (injetados só aqui) ---- */
/* Sem contorno externo: o formulário fica limpo sobre o fundo */
[data-testid="stForm"] {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
    padding: 0 !important;
}
/* Campos maiores */
[data-baseweb="input"], [data-baseweb="base-input"] {
    min-height: 52px !important;
}
[data-testid="stTextInput"] input {
    font-size: 1.05rem !important;
}
[data-testid="stTextInput"] label {
    font-size: 1rem !important;
    font-weight: 600 !important;
    margin-bottom: 2px !important;
}
/* Botão Entrar maior */
[data-testid="stFormSubmitButton"] button {
    padding: .85rem 1.4rem !important;
    font-size: 1.1rem !important;
    border-radius: 12px !important;
    margin-top: .4rem;
}
/* Badge da logo maior e centralizado (margin auto garante o centro
   mesmo se o contêiner flex não se aplicar ao HTML renderizado) */
.auth-badge {
    width: 74px !important;
    height: 74px !important;
    border-radius: 22px !important;
    font-size: 32px !important;
    margin: 0 auto !important;
}
</style>
"""


def login_page():
    st.markdown(_LOGIN_CSS, unsafe_allow_html=True)
    # Espaço no topo para centralizar verticalmente
    st.markdown('<div style="height:7vh"></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.6, 1])
    with col:
        st.markdown(
            '<div style="display:flex;flex-direction:column;align-items:center;'
            'text-align:center;margin-bottom:1.75rem;">'
            '<div class="auth-badge">D</div>'
            '<div style="margin:1rem 0 0;font-size:1.9rem;font-weight:800;color:#0F172A;'
            'text-align:center;width:100%;">DoaNet</div>'
            '<p style="color:#6B7280;margin:.35rem 0 0;font-size:1.05rem;'
            'text-align:center;width:100%;">Painel do Administrador</p>'
            '</div>',
            unsafe_allow_html=True,
        )

        has_admins = check_first_admin()
        if has_admins is None:
            st.error(f"Backend indisponível em {BACKEND_URL}. Inicie o servidor e recarregue.")
            return
        if not has_admins:
            register_first_admin()
            return

        with st.form("login_form"):
            email = st.text_input("E-mail", placeholder="voce@exemplo.com")
            password = st.text_input("Senha", type="password", placeholder="••••••••")
            submitted = st.form_submit_button("Entrar", width='stretch')
            if submitted:
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/login",
                        json={"email": email, "password": password},
                        timeout=10,
                    )
                except requests.exceptions.RequestException:
                    st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}).")
                    return

                if response.status_code == 200:
                    data = response.json()
                    admin = data.get("admin", {})
                    st.session_state.update(
                        logged_in=True,
                        token=data["access_token"],
                        admin_name=admin.get("name"),
                        admin_email=admin.get("email"),
                        admin_role=admin.get("role"),
                        admin_org_id=admin.get("org_id"),
                    )
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")


def register_first_admin():
    st.info("Nenhum administrador cadastrado. Crie o administrador principal.")
    with st.form("register_form"):
        name = st.text_input("Nome")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        confirm = st.text_input("Confirmar senha", type="password")
        submitted = st.form_submit_button("Criar Administrador Principal")
        if submitted:
            if password != confirm:
                st.error("As senhas não conferem")
            elif not (name and email and password):
                st.error("Preencha todos os campos")
            else:
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/admin/register-first",
                        json={"name": name, "email": email, "password": password},
                        timeout=10,
                    )
                except requests.exceptions.RequestException:
                    st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}).")
                    return
                if response.status_code == 200:
                    st.success("Administrador principal criado! Faça login.")
                    st.rerun()
                else:
                    st.error(error_detail(response))
