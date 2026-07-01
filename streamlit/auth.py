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


def login_page():
    col = st.columns([1, 1.3, 1])[1]
    with col:
        st.markdown(
            '<div class="auth-badge">D</div>'
            '<h2 style="text-align:center;margin:0;">DoaNet</h2>'
            '<p style="text-align:center;color:#6B7280;margin:.2rem 0 1.4rem;">'
            'Painel do Administrador</p>',
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
            submitted = st.form_submit_button("Entrar")
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
