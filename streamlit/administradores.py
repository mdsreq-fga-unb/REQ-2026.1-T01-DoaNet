"""Gerenciamento de administradores (restrito ao administrador principal)."""
import streamlit as st

from config import DEFAULT_ORG_ID
from api import make_request, error_detail
from ui import flash, show_flash


def admins_page():
    st.subheader("Administradores")
    if st.session_state.get("admin_role") != "master":
        st.warning("Acesso restrito. Apenas o administrador principal pode gerenciar admins.")
        return

    show_flash()

    tab_create, tab_manage = st.tabs(["Novo admin", "Gerenciar"])

    with tab_create:
        with st.form("create_admin", clear_on_submit=True):
            name = st.text_input("Nome")
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("Criar administrador"):
                if not (name and email and password):
                    st.error("Preencha todos os campos.")
                else:
                    with st.spinner("Criando administrador..."):
                        resp = make_request("POST", "/admin/create", {
                            "name": name,
                            "email": email,
                            "password": password,
                            "org_id": DEFAULT_ORG_ID,
                        })
                    if resp is not None and resp.status_code == 200:
                        flash("Administrador criado!")
                        st.rerun()
                    elif resp is not None:
                        st.error(error_detail(resp))

    with tab_manage:
        resp = make_request("GET", "/admin/list")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return
        admins = resp.json().get("admins", [])
        for admin in admins:
            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                role_pill = "pill-evento" if admin["role"] == "master" else "pill-post"
                status = "Ativo" if admin["is_active"] else "Inativo"
                c1.markdown(
                    f'<span class="pill {role_pill}">{admin["role"]}</span>'
                    f'<div class="card-title">{admin["name"]}</div>'
                    f'<div class="card-meta">{admin["email"]} · {status}</div>'
                    + (f'<div class="card-meta">{admin["org_id"]}</div>' if admin.get("org_id") else ''),
                    unsafe_allow_html=True,
                )
                if admin["role"] != "master" and admin["is_active"]:
                    if c2.button("Desativar", key=f"deact_{admin['id']}"):
                        with st.spinner("Desativando..."):
                            r = make_request("DELETE", f"/admin/{admin['id']}")
                        if r is not None and r.status_code == 200:
                            flash("Admin desativado!")
                            st.rerun()
                        elif r is not None:
                            st.error(error_detail(r))
