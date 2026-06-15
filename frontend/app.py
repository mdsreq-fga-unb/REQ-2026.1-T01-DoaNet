import streamlit as st
import requests
from datetime import datetime

# URL do seu backend FastAPI
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Portal da ONG", page_icon="🤝")

# Inicializa session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'token' not in st.session_state:
    st.session_state['token'] = None
if 'admin_name' not in st.session_state:
    st.session_state['admin_name'] = None
if 'admin_email' not in st.session_state:
    st.session_state['admin_email'] = None

def check_first_admin():
    """Verifica se já existe algum administrador cadastrado"""
    try:
        response = requests.get(f"{BACKEND_URL}/admin/check-first")
        if response.status_code == 200:
            data = response.json()
            return data['has_admins'], data['count']
        return False, 0
    except:
        return False, 0

def register_admin_page():
    """Página de registro do primeiro administrador"""
    st.title("🆕 Configuração Inicial")
    st.write("Crie o primeiro administrador do sistema")
    
    has_admins, count = check_first_admin()
    
    if has_admins and count > 0:
        st.success("Já existem administradores cadastrados!")
        st.info("Volte para a página de login")
        if st.button("Ir para Login"):
            st.session_state['show_register'] = False
            st.rerun()
        return
    
    with st.form("register_form"):
        st.subheader("Dados do Administrador")
        name = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        confirm_password = st.text_input("Confirmar senha", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("Criar Administrador", type="primary")
        with col2:
            if st.form_submit_button("Cancelar"):
                st.session_state['show_register'] = False
                st.rerun()
        
        if submit:
            if not all([name, email, password]):
                st.error("Preencha todos os campos")
                return
            
            if password != confirm_password:
                st.error("As senhas não conferem")
                return
            
            try:
                response = requests.post(
                    f"{BACKEND_URL}/admin/register",
                    json={
                        "name": name,
                        "email": email,
                        "password": password,
                        "secret_key": ""  # ✅ Envia string vazia ao invés de None
                    }
                )

                if response.status_code == 200:
                    st.success("Administrador criado com sucesso!")
                    st.info("Faça login para continuar")
                    if st.button("Ir para Login"):
                        st.session_state['show_register'] = False
                        st.rerun()
                else:
                    error = response.json().get('detail', 'Erro desconhecido')
                    st.error(f"Erro ao criar admin: {error}")
            except requests.exceptions.ConnectionError:
                st.error("Erro de conexão com o backend")

def login_page():
    """Página de login"""
    st.title("🔐 Acesso ao Sistema")
    st.write("Insira suas credenciais para gerenciar a plataforma")
    
    # Botão para criar primeiro admin se não existir
    has_admins, count = check_first_admin()
    if not has_admins:
        st.warning("⚠️ Nenhum administrador cadastrado ainda!")
        if st.button("Criar Primeiro Administrador"):
            st.session_state['show_register'] = True
            st.rerun()
        return
    
    with st.form("login_form"):
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button("Entrar", type="primary")
        
        if submit_button:
            if not email or not password:
                st.warning("Por favor, preencha todos os campos.")
                return
            
            try:
                response = requests.post(
                    f"{BACKEND_URL}/login",
                    json={"email": email, "password": password}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Login realizado com sucesso!")
                    
                    # Salva informações na sessão
                    st.session_state['logged_in'] = True
                    st.session_state['token'] = data.get("access_token")
                    st.session_state['admin_name'] = data.get('admin', {}).get('name')
                    st.session_state['admin_email'] = data.get('admin', {}).get('email')
                    
                    st.rerun()
                else:
                    st.error("E-mail ou senha incorretos.")
            
            except requests.exceptions.ConnectionError:
                st.error("Erro de conexão: O backend FastAPI está rodando?")

def main_dashboard():
    """Dashboard principal após login"""
    st.title("📊 Painel de Controle")
    st.write(f"Bem-vindo, {st.session_state.get('admin_name', 'Administrador')}!")
    st.write(f"Email: {st.session_state.get('admin_email', '')}")
    
    # Sidebar com informações
    with st.sidebar:
        st.image("https://via.placeholder.com/150x150?text=ONG", width=150)
        st.markdown("---")
        st.subheader("Menu")
        
        menu_option = st.radio(
            "Navegação",
            ["Dashboard", "Feed de Notícias", "Minha Conta"]
        )
        
        st.markdown("---")
        if st.button("🚪 Sair", type="secondary"):
            st.session_state['logged_in'] = False
            st.session_state['token'] = None
            st.session_state['admin_name'] = None
            st.session_state['admin_email'] = None
            st.rerun()
    
    # Conteúdo principal baseado no menu
    if menu_option == "Dashboard":
        show_dashboard()
    elif menu_option == "Feed de Notícias":
        show_feed_management()
    elif menu_option == "Minha Conta":
        show_account_settings()

def show_dashboard():
    """Exibe o dashboard com métricas"""
    st.subheader("Métricas da ONG")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Doações", value="R$ 0,00", delta="Este mês")
    with col2:
        st.metric(label="Itens no Feed", value="0")
    with col3:
        st.metric(label="Visitas", value="0")
    
    st.info("Configure seu backend para exibir métricas reais do MongoDB")

def show_feed_management():
    """Gerencia o feed de notícias"""
    st.subheader("Gerenciar Feed de Notícias")
    
    token = st.session_state.get('token')
    headers = {"Authorization": f"Bearer {token}"}
    
    # Abas para visualizar e criar
    tab1, tab2 = st.tabs(["📋 Visualizar Feed", "➕ Criar Novo Item"])
    
    with tab1:
        try:
            response = requests.get(f"{BACKEND_URL}/feed", headers=headers)
            if response.status_code == 200:
                feed_items = response.json()
                if feed_items:
                    for item in feed_items:
                        with st.expander(f"{item.get('title', 'Sem título')}"):
                            st.write(f"**Tipo:** {item.get('type', 'N/A')}")
                            st.write(f"**Conteúdo:** {item.get('content', 'N/A')}")
                            if st.button(f"Excluir", key=f"delete_{item.get('id')}"):
                                delete_response = requests.delete(
                                    f"{BACKEND_URL}/feed/{item.get('id')}",
                                    headers=headers
                                )
                                if delete_response.status_code == 200:
                                    st.success("Item excluído!")
                                    st.rerun()
                else:
                    st.info("Nenhum item no feed")
            else:
                st.error("Erro ao carregar feed")
        except Exception as e:
            st.error(f"Erro: {str(e)}")
    
    with tab2:
        with st.form("create_feed_item"):
            title = st.text_input("Título")
            item_type = st.selectbox("Tipo", ["evento", "noticia", "campanha"])
            content = st.text_area("Conteúdo")
            
            if st.form_submit_button("Publicar"):
                if title and content:
                    new_item = {
                        "title": title,
                        "type": item_type,
                        "content": content,
                        "created_at": datetime.now().isoformat()
                    }
                    response = requests.post(
                        f"{BACKEND_URL}/feed",
                        json=new_item,
                        headers=headers
                    )
                    if response.status_code == 200:
                        st.success("Item publicado com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao publicar item")
                else:
                    st.warning("Preencha todos os campos")

def show_account_settings():
    """Configurações da conta"""
    st.subheader("Configurações da Conta")
    
    st.write(f"**Nome:** {st.session_state.get('admin_name')}")
    st.write(f"**Email:** {st.session_state.get('admin_email')}")
    
    st.info("Funcionalidade de alteração de senha em desenvolvimento")

# Roteamento principal
if 'show_register' not in st.session_state:
    st.session_state['show_register'] = False

if st.session_state.get('show_register'):
    register_admin_page()
elif st.session_state.get('logged_in'):
    main_dashboard()
else:
    login_page()