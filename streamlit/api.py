"""Helpers de comunicação HTTP com o backend."""
import requests
import streamlit as st

from config import BACKEND_URL


def _headers():
    return {"Authorization": f"Bearer {st.session_state['token']}"}


def make_request(method, endpoint, data=None):
    """Requisição autenticada ao backend. Retorna o objeto Response ou None."""
    url = f"{BACKEND_URL}{endpoint}"
    try:
        if method == "GET":
            return requests.get(url, headers=_headers(), timeout=10)
        if method == "POST":
            return requests.post(url, json=data, headers=_headers(), timeout=10)
        if method == "PUT":
            return requests.put(url, json=data, headers=_headers(), timeout=10)
        if method == "DELETE":
            return requests.delete(url, headers=_headers(), timeout=10)
    except requests.exceptions.RequestException:
        st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}). Ele está rodando?")
        return None


def error_detail(response):
    """Extrai uma mensagem de erro legível de uma resposta."""
    if response is None:
        return "Sem resposta do servidor"
    try:
        payload = response.json()
        detail = payload.get("detail", payload)
        if isinstance(detail, list):  # erros de validação do FastAPI
            return "; ".join(d.get("msg", str(d)) for d in detail)
        return str(detail)
    except Exception:
        return f"Erro {response.status_code}"


def make_multipart_request(method, endpoint, data=None, files=None):
    """Requisição multipart/form-data ao backend (usada pelo /feed)."""
    url = f"{BACKEND_URL}{endpoint}"
    try:
        if method == "POST":
            return requests.post(url, data=data, files=files, headers=_headers(), timeout=30)
        if method == "PUT":
            return requests.put(url, data=data, files=files, headers=_headers(), timeout=30)
    except requests.exceptions.RequestException:
        st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}). Ele está rodando?")
        return None


def feed_result_ok(resp):
    """O /feed responde 200 mesmo em falha (corpo {'error':..., 'status':'failed'}).
    Retorna (ok, mensagem)."""
    if resp is None:
        return False, "Sem resposta do servidor"
    if resp.status_code != 200:
        return False, error_detail(resp)
    try:
        body = resp.json()
    except Exception:
        return True, ""
    if isinstance(body, dict) and (body.get("status") == "failed" or body.get("error")):
        return False, body.get("error", "Falha na operação")
    return True, ""
