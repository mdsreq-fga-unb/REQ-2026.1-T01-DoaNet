"""Painel administrativo DoaNet — ponto de entrada.

A aplicação foi dividida em módulos por responsabilidade:
  config.py          — constantes e estado de sessão
  api.py             — helpers de requisição ao backend
  styles.py          — CSS/identidade visual
  auth.py            — login e cadastro do admin principal
  publicacoes.py     — posts e eventos do feed
  oportunidades.py   — vagas de voluntariado
  financeiro.py      — doações, despesas e transparência
  administradores.py — gestão de admins
  organizacao.py     — configuração da organização
  dashboard.py       — navegação e roteamento das seções
"""
import streamlit as st

# set_page_config precisa ser o primeiro comando Streamlit executado.
st.set_page_config(
    page_title="DoaNet · Admin",
    layout="wide",
    initial_sidebar_state="expanded",
)

from config import init_session_state
from styles import inject_css
from auth import login_page
from dashboard import main_dashboard

init_session_state()
inject_css()

if not st.session_state.get("logged_in"):
    login_page()
else:
    main_dashboard()
