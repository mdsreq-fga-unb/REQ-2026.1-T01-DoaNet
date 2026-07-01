"""Dashboard principal — hero, navegação lateral e roteamento das seções."""
import streamlit as st

from config import DEFAULTS
from publicacoes import publicacoes_section
from oportunidades import oportunidades_section
from financeiro import financeiro_section
from organizacao import organizacao_section
from administradores import admins_page


def main_dashboard():
    role_label = ("Administrador Principal"
                  if st.session_state["admin_role"] == "master" else "Administrador")
    st.markdown(
        f'<div class="hero"><h1>Olá, {st.session_state["admin_name"]}</h1>'
        f'<p>{role_label} · Painel de gestão DoaNet</p></div>',
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.markdown(
            '<div class="side-brand">'
            '<span class="side-logo">D</span>'
            '<span class="side-name">DoaNet</span>'
            '</div>'
            f'<span class="side-email">{st.session_state.get("admin_email", "")}</span>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
        menu = st.radio(
            "Navegação",
            ["Publicações", "Oportunidades", "Financeiro", "Organização", "Administradores", "Sobre"],
            label_visibility="collapsed",
        )
        st.markdown("---")
        if st.button("Sair", width='stretch'):
            for key in DEFAULTS:
                st.session_state[key] = DEFAULTS[key]
            st.rerun()

    if menu == "Publicações":
        publicacoes_section()
    elif menu == "Oportunidades":
        oportunidades_section()
    elif menu == "Financeiro":
        financeiro_section()
    elif menu == "Organização":
        organizacao_section()
    elif menu == "Administradores":
        admins_page()
    else:
        st.subheader("Sobre")
        st.write("Sistema de gerenciamento da ONG — publique posts, eventos e oportunidades de voluntariado.")
