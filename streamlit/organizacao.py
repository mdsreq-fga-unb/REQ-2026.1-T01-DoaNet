"""Configuração da organização (identidade visual, logo)."""
import requests
import streamlit as st

from config import BACKEND_URL, DEFAULT_ORG_ID
from api import make_multipart_request, error_detail
from ui import flash, show_flash


def organizacao_section():
    st.subheader("Minha Organização")
    show_flash()

    org_id = st.session_state.get("admin_org_id") or DEFAULT_ORG_ID  # <- fallback
    st.caption(f"Configurando: **{org_id}**")

    resp = requests.get(f"{BACKEND_URL}/orgs/{org_id}/config", timeout=10)
    current = resp.json() if resp.status_code == 200 else {}

    with st.form("org_config_form"):
        name = st.text_input("Nome da organização", value=current.get("name", ""))
        description = st.text_area("Descrição", value=current.get("description", ""), height=120)

        col1, col2 = st.columns(2)
        primary_color = col1.text_input(
            "Cor primária (hex)",
            value=current.get("primary_color", "#0088FF"),
            placeholder="#0088FF"
        )
        background_color = col2.text_input(
            "Cor de fundo (hex)",
            value=current.get("background_color", "#FFFFFF"),
            placeholder="#FFFFFF"
        )

        if primary_color:
            st.markdown(
                f'<div style="display:flex;gap:12px;margin:8px 0;">'
                f'<div style="background:{primary_color};width:36px;height:36px;'
                f'border-radius:8px;border:1px solid #eee;"></div>'
                f'<div style="background:{background_color};width:36px;height:36px;'
                f'border-radius:8px;border:1px solid #eee;"></div>'
                f'<span style="color:#6B7280;font-size:.85rem;align-self:center;">'
                f'Primária · Fundo</span></div>',
                unsafe_allow_html=True,
            )

        if current.get("logo_url"):
            st.image(current["logo_url"], width=120, caption="Logo atual")

        logo = st.file_uploader(
            "Logo da organização (opcional — mantém o atual se vazio)",
            type=["png", "jpg", "jpeg", "webp"],
        )

        data = {
            "org_id": org_id,
            "name": name,
            "description": description,
            "primary_color": primary_color,
            "background_color": background_color or "#FFFFFF",
        }
        files = None
        if logo is not None:
            files = {"logo": (logo.name, logo.getvalue(), logo.type)}

        if st.form_submit_button("Salvar configurações"):
            if not (name and description and primary_color):
                st.error("Preencha nome, descrição e cor primária.")
            else:
                with st.spinner("Salvando configurações..."):
                    r = make_multipart_request("POST", "/orgs", data=data, files=files)
                if r is not None and r.status_code == 200:
                    flash("Configurações salvas! O app já reflete as mudanças.")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))
