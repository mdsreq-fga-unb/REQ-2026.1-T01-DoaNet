"""Helpers de feedback visual.

O padrão de ação no painel é: enviar a requisição e, em caso de sucesso,
chamar st.rerun() (o form volta limpo). O problema é que st.success/st.error
são apagados por esse rerun, então o usuário não vê confirmação alguma.

flash() guarda a mensagem no session_state antes do rerun e show_flash()
a exibe (uma única vez) no topo da seção após o recarregamento.
"""
import streamlit as st

_FLASH_KEY = "_flash_message"

_ICONS = {"success": "✅", "error": "❌", "info": "ℹ️", "warning": "⚠️"}


def flash(message, kind="success"):
    """Registra uma mensagem para ser exibida logo após o próximo st.rerun()."""
    st.session_state[_FLASH_KEY] = (message, kind)


def show_flash():
    """Exibe (e consome) a mensagem pendente registrada por flash()."""
    data = st.session_state.pop(_FLASH_KEY, None)
    if not data:
        return
    message, kind = data
    icon = _ICONS.get(kind, "✅")
    # Toast: popup temporário no canto (chama atenção imediata).
    try:
        st.toast(message, icon=icon)
    except Exception:
        pass
    # Banner: permanece visível no topo da seção até a próxima interação.
    getattr(st, kind, st.success)(message)
