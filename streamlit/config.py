"""Configurações globais e estado de sessão do painel administrativo."""
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000"

# Single-org por enquanto: id único padronizado (ver domain/constants.py no backend).
DEFAULT_ORG_ID = "move-educa"

# A coleção org_feed guarda 2 tipos de publicação: "post" e "evento".
# Ambos compartilham os mesmos campos (title, type, description, image_url, image_path).
FEED_TYPES = ["post", "evento"]
FEED_TYPE_META = {
    "post": ("Post", "pill-post"),
    "evento": ("Evento", "pill-evento"),
}

# Valores iniciais do estado de sessão relacionados à autenticação.
DEFAULTS = {
    "logged_in": False,
    "token": None,
    "admin_name": None,
    "admin_email": None,
    "admin_role": None,
    "admin_org_id": None,
}


def init_session_state():
    """Garante que as chaves de autenticação existam no session_state."""
    for _k, _v in DEFAULTS.items():
        st.session_state.setdefault(_k, _v)
