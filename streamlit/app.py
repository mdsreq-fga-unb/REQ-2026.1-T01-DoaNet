import streamlit as st
import requests
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="ONG - Admin", page_icon="🏢", layout="wide")

# Inicializa session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'token' not in st.session_state:
    st.session_state['token'] = None
if 'admin_name' not in st.session_state:
    st.session_state['admin_name'] = None
if 'admin_email' not in st.session_state:
    st.session_state['admin_email'] = None
if 'admin_role' not in st.session_state:
    st.session_state['admin_role'] = None

def make_request(method, endpoint, data=None):
    headers = {"Authorization": f"Bearer {st.session_state['token']}"}
    url = f"{BACKEND_URL}{endpoint}"

    if method == "GET":
        return requests.get(url, headers=headers)
    elif method == "POST":
        return requests.post(url, json=data, headers=headers)
    elif method == "PUT":
        return requests.put(url, json=data, headers=headers)
    elif method == "DELETE":
        return requests.delete(url, headers=headers)

def login_page():
    st.title("🔐 Acesso ao Sistema")

    has_admins = check_first_admin()
    if not has_admins:
        register_first_admin()
        return

    with st.form("login_form"):
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/login",
                    json={"email": email, "password": password}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.session_state['logged_in'] = True
                    st.session_state['token'] = data["access_token"]
                    st.session_state['admin_name'] = data.get('admin', {}).get('name')
                    st.session_state['admin_email'] = data.get('admin', {}).get('email')
                    st.session_state['admin_role'] = data.get('admin', {}).get('role')
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")
            except Exception as e:
                st.error(f"Erro: {e}")

def register_first_admin():
    st.title("🆕 Configuração Inicial")
    st.write("Crie o administrador principal")

    with st.form("register_form"):
        name = st.text_input("Nome")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        confirm = st.text_input("Confirmar senha", type="password")

        if st.form_submit_button("Criar Administrador Principal"):
            if password != confirm:
                st.error("Senhas não conferem")
            else:
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/admin/register-first",
                        json={"name": name, "email": email, "password": password}
                    )
                    if response.status_code == 200:
                        st.success("Admin principal criado! Faça login.")
                        st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

def check_first_admin():
    try:
        response = requests.get(f"{BACKEND_URL}/admin/check-first")
        return response.json().get('has_admins', False)
    except:
        return False

def events_page():
    st.header("📅 Gerenciar Eventos")

    tab1, tab2 = st.tabs(["➕ Criar Evento", "📋 Listar Eventos"])

    with tab1:
        with st.form("create_event"):
            title = st.text_input("Título do Evento")
            description = st.text_area("Descrição")
            date = st.date_input("Data do Evento")
            time = st.time_input("Horário")
            location = st.text_input("Local")
            max_participants = st.number_input("Máximo de participantes", min_value=1, value=100)
            image_url = st.text_input("URL da imagem (opcional)")

            if st.form_submit_button("Criar Evento"):
                event_data = {
                    "title": title,
                    "description": description,
                    "date": datetime.combine(date, time).isoformat(),
                    "location": location,
                    "max_participants": max_participants,
                    "image_url": image_url
                }
                response = make_request("POST", "/events", event_data)
                if response.status_code == 200:
                    st.success("Evento criado com sucesso!")
                    st.rerun()
                else:
                    st.error(f"Erro: {response.json().get('detail', 'Erro desconhecido')}")

    with tab2:
        response = make_request("GET", "/events")
        if response.status_code == 200:
            events = response.json().get('events', [])
            for event in events:
                with st.expander(f"{event['title']} - {event['date'][:10]}"):
                    st.write(f"**Descrição:** {event['description']}")
                    st.write(f"**Local:** {event['location']}")
                    st.write(f"**Participantes:** {event['current_participants']}/{event['max_participants'] or '∞'}")
                    if st.button(f"Registrar participante", key=f"reg_{event['id']}"):
                        reg_response = make_request("POST", f"/events/{event['id']}/register")
                        if reg_response.status_code == 200:
                            st.success("Participante registrado!")
                            st.rerun()

                    if st.session_state.get('admin_role') == 'master':
                        if st.button(f"❌ Deletar", key=f"del_{event['id']}"):
                            del_response = make_request("DELETE", f"/events/{event['id']}")
                            if del_response.status_code == 200:
                                st.success("Evento deletado!")
                                st.rerun()
        else:
            st.error("Erro ao carregar eventos")

def admins_page():
    st.header("👥 Gerenciar Administradores")

    if st.session_state.get('admin_role') != 'master':
        st.error(f"Acesso negado. Apenas administradores principais podem gerenciar admins. Seu role é: {st.session_state.get('admin_role')}")
        return

    tab1, tab2 = st.tabs(["➕ Criar Admin", "📋 Listar Admins"])

    with tab1:
        with st.form("create_admin"):
            name = st.text_input("Nome")
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")

            if st.form_submit_button("Criar Administrador"):
                response = make_request("POST", "/admin/create", {
                    "name": name, "email": email, "password": password
                })
                if response.status_code == 200:
                    st.success("Administrador criado!")
                    st.rerun()
                else:
                    st.error(f"Erro: {response.json().get('detail', 'Erro desconhecido')}")

    with tab2:
        response = make_request("GET", "/admin/list")
        if response.status_code == 200:
            admins = response.json().get('admins', [])
            for admin in admins:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{admin['name']}** - {admin['email']}")
                    st.write(f"Role: {admin['role']} | Status: {'Ativo' if admin['is_active'] else 'Inativo'}")
                with col2:
                    if admin['role'] != 'master' and admin['is_active']:
                        if st.button(f"Desativar", key=f"deact_{admin['id']}"):
                            del_response = make_request("DELETE", f"/admin/{admin['id']}")
                            if del_response.status_code == 200:
                                st.success("Admin desativado!")
                                st.rerun()
                with col3:
                    if admin['role'] != 'master' and not admin['is_active']:
                        st.write("❌ Inativo")
        else:
            st.error("Erro ao carregar admins")

def main_dashboard():
    st.title(f"🏢 Bem-vindo, {st.session_state['admin_name']}!")
    st.write(f"Role: {'Administrador Principal' if st.session_state['admin_role'] == 'master' else 'Administrador'}")

    with st.sidebar:
        st.image("https://via.placeholder.com/150x150?text=ONG", width=150)
        st.markdown("---")
        menu = st.radio(
            "Navegação",
            ["📅 Eventos", "👥 Administradores", "ℹ️ Sobre"]
        )

        if st.button("🚪 Sair"):
            for key in ['logged_in', 'token', 'admin_name', 'admin_email', 'admin_role']:
                st.session_state[key] = None
            st.rerun()

    if menu == "📅 Eventos":
        events_page()
    elif menu == "👥 Administradores":
        admins_page()
    else:
        st.info("Sistema de gerenciamento da ONG")

# Roteamento principal
if not st.session_state.get('logged_in'):
    login_page()
else:
    main_dashboard()
