# frontend/app.py
import streamlit as st
import requests

# URL do seu backend FastAPI (ajuste a porta se necessário)
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Portal da ONG", page_icon="🌍")

def login_page():
    st.title("Acesso ao Sistema")
    st.write("Insira suas credenciais para gerenciar a plataforma.")

    with st.form("login_form"):
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button("Entrar")

    if submit_button:
        if not email or not password:
            st.warning("Por favor, preencha todos os campos.")
            return

        # Faz a requisição HTTP para o seu backend FastAPI
        try:
            response = requests.post(
                f"{BACKEND_URL}/login", 
                json={"email": email, "password": password}
            )

            if response.status_code == 200:
                data = response.json()
                st.success("Login realizado com sucesso!")
                
                # Salva o status de login e o token na sessão do Streamlit
                st.session_state['logged_in'] = True
                st.session_state['token'] = data.get("token")
                
                # Recarrega a página para mostrar a área logada
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")
                
        except requests.exceptions.ConnectionError:
            st.error("Erro de conexão: O backend FastAPI está rodando?")

def main_dashboard():
    st.title("Painel de Controle")
    st.write("Bem-vindo à área de gestão da ONG!")
    st.write(f"Seu Token de Sessão: {st.session_state.get('token')}")
    
    if st.button("Sair"):
        st.session_state['logged_in'] = False
        st.session_state['token'] = None
        st.rerun()

# Lógica de roteamento simples do Streamlit
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    main_dashboard()
else:
    login_page()

def acessar_area_restrita():
    st.subheader("Resumo de Doações")
    
    token = st.session_state.get('token')
    
    # Configura o cabeçalho com o JWT
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Faz um GET na rota protegida
    response = requests.get(f"{BACKEND_URL}/doacoes/resumo", headers=headers)
    
    if response.status_code == 200:
        dados = response.json()
        st.success(dados["message"])
        st.metric(label="Doações do Mês", value=f"R$ {dados['doacoes_mes']}")
    elif response.status_code == 401:
        st.error("Sua sessão expirou ou é inválida. Por favor, faça login novamente.")
        st.session_state['logged_in'] = False
        st.rerun()