import streamlit as st
import requests
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000"

# A coleção org_feed guarda 2 tipos de publicação: "post" e "evento".
# Ambos compartilham os mesmos campos (title, type, description, image_url, image_path).
FEED_TYPES = ["post", "evento"]
FEED_TYPE_META = {
    "post": ("Post", "📝", "pill-post"),
    "evento": ("Evento", "📅", "pill-evento"),
}

st.set_page_config(
    page_title="DoaNet · Admin",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
_defaults = {
    "logged_in": False,
    "token": None,
    "admin_name": None,
    "admin_email": None,
    "admin_role": None,
}
for _k, _v in _defaults.items():
    st.session_state.setdefault(_k, _v)


# ----------------------------------------------------------------------------
# Estilo
# ----------------------------------------------------------------------------
def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"], button, input, textarea, select {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .block-container { padding-top: 2.2rem; max-width: 1100px; }

        /* ---- Hero ---- */
        .hero {
            background: linear-gradient(135deg, #FF4B4B 0%, #FF6B6B 55%, #FF8E53 100%);
            padding: 26px 32px; border-radius: 20px; color: #fff;
            box-shadow: 0 14px 34px rgba(255,75,75,.28);
            margin-bottom: 22px;
        }
        .hero h1 { color:#fff; font-size:1.55rem; font-weight:800; margin:0; letter-spacing:-.4px; }
        .hero p  { color:rgba(255,255,255,.92); margin:6px 0 0; font-size:.95rem; }

        /* ---- Auth ---- */
        .auth-badge {
            width:64px; height:64px; border-radius:18px; margin:0 auto 14px;
            display:flex; align-items:center; justify-content:center; font-size:32px;
            background:linear-gradient(135deg,#FF4B4B,#FF8E53);
            box-shadow:0 10px 24px rgba(255,75,75,.3);
        }

        /* ---- Pills ---- */
        .pill { display:inline-block; padding:3px 12px; border-radius:999px;
            font-size:.70rem; font-weight:700; letter-spacing:.4px; text-transform:uppercase; }
        .pill-post     { background:#E7F0FF; color:#2563EB; }
        .pill-evento   { background:#FFECEC; color:#E11D48; }
        .pill-vaga     { background:#E7F9EE; color:#16A34A; }
        .pill-inactive { background:#F1F3F7; color:#94A3B8; }

        .card-title { font-size:1.06rem; font-weight:700; color:#1F2330; margin:6px 0 2px; }
        .card-meta  { color:#6B7280; font-size:.83rem; margin-bottom:6px; }
        .card-body  { color:#374151; font-size:.92rem; line-height:1.5; }

        /* ---- Buttons ---- */
        .stButton > button { border-radius:10px; font-weight:600; transition:all .15s ease; }
        .stButton > button:hover { transform:translateY(-1px); }
        [data-testid="stFormSubmitButton"] button {
            background:linear-gradient(135deg,#FF4B4B,#FF6B6B); color:#fff; border:none;
            border-radius:10px; font-weight:700; padding:.55rem 1.4rem; width:100%;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            box-shadow:0 8px 20px rgba(255,75,75,.32); transform:translateY(-1px);
        }

        /* ---- Inputs ---- */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stNumberInput"] input { border-radius:10px; }

        /* ---- Sidebar ---- */
        section[data-testid="stSidebar"] { background:#FAFBFC; border-right:1px solid #EDF0F4; }

        /* ---- Tabs ---- */
        .stTabs [data-baseweb="tab-list"] { gap:6px; }
        .stTabs [data-baseweb="tab"] { border-radius:10px 10px 0 0; padding:8px 16px; font-weight:600; }

        #MainMenu, footer { visibility:hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------------
# HTTP helpers
# ----------------------------------------------------------------------------
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
        st.error(f"⚠️ Não foi possível conectar ao backend ({BACKEND_URL}). Ele está rodando?")
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


# ----------------------------------------------------------------------------
# Autenticação
# ----------------------------------------------------------------------------
def check_first_admin():
    try:
        response = requests.get(f"{BACKEND_URL}/admin/check-first", timeout=10)
        return response.json().get("has_admins", False)
    except requests.exceptions.RequestException:
        return None  # backend offline


def login_page():
    col = st.columns([1, 1.3, 1])[1]
    with col:
        st.markdown(
            '<div class="auth-badge">❤️</div>'
            '<h2 style="text-align:center;margin:0;">DoaNet</h2>'
            '<p style="text-align:center;color:#6B7280;margin:.2rem 0 1.4rem;">'
            'Painel do Administrador</p>',
            unsafe_allow_html=True,
        )

        has_admins = check_first_admin()
        if has_admins is None:
            st.error(f"⚠️ Backend indisponível em {BACKEND_URL}. Inicie o servidor e recarregue.")
            return
        if not has_admins:
            register_first_admin()
            return

        with st.form("login_form"):
            email = st.text_input("E-mail", placeholder="voce@exemplo.com")
            password = st.text_input("Senha", type="password", placeholder="••••••••")
            submitted = st.form_submit_button("Entrar")
            if submitted:
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/login",
                        json={"email": email, "password": password},
                        timeout=10,
                    )
                except requests.exceptions.RequestException:
                    st.error(f"⚠️ Não foi possível conectar ao backend ({BACKEND_URL}).")
                    return

                if response.status_code == 200:
                    data = response.json()
                    admin = data.get("admin", {})
                    st.session_state.update(
                        logged_in=True,
                        token=data["access_token"],
                        admin_name=admin.get("name"),
                        admin_email=admin.get("email"),
                        admin_role=admin.get("role"),
                    )
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")


def register_first_admin():
    st.info("Nenhum administrador cadastrado. Crie o administrador principal.")
    with st.form("register_form"):
        name = st.text_input("Nome")
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        confirm = st.text_input("Confirmar senha", type="password")
        submitted = st.form_submit_button("Criar Administrador Principal")
        if submitted:
            if password != confirm:
                st.error("As senhas não conferem")
            elif not (name and email and password):
                st.error("Preencha todos os campos")
            else:
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/admin/register-first",
                        json={"name": name, "email": email, "password": password},
                        timeout=10,
                    )
                except requests.exceptions.RequestException:
                    st.error(f"⚠️ Não foi possível conectar ao backend ({BACKEND_URL}).")
                    return
                if response.status_code == 200:
                    st.success("Administrador principal criado! Faça login.")
                    st.rerun()
                else:
                    st.error(error_detail(response))


# ----------------------------------------------------------------------------
# Publicações (org_feed) — posts e eventos
# ----------------------------------------------------------------------------
def publicacoes_section():
    st.subheader("📋 Publicações")
    st.caption("Posts e eventos do feed (coleção org_feed). Ambos suportam imagem.")

    tab_create, tab_manage = st.tabs(["➕ Nova publicação", "🗂️ Gerenciar"])

    with tab_create:
        with st.form("create_feed", clear_on_submit=True):
            ptype = st.radio(
                "Tipo de publicação",
                FEED_TYPES,
                horizontal=True,
                format_func=lambda t: f"{FEED_TYPE_META[t][1]} {FEED_TYPE_META[t][0]}",
            )
            title = st.text_input("Título")
            description = st.text_area("Descrição", height=130)
            image_url = st.text_input("URL da imagem (image_url)")
            image_path = st.text_input("Caminho da imagem (image_path)")
            if st.form_submit_button("Publicar"):
                if not (title and description):
                    st.error("Preencha título e descrição.")
                else:
                    payload = {
                        "title": title,
                        "type": ptype,
                        "description": description,
                        "image_url": image_url or None,
                        "image_path": image_path or None,
                    }
                    resp = make_request("POST", "/feed", payload)
                    if resp is not None and resp.status_code == 200:
                        st.success("Publicação criada com sucesso!")
                        st.rerun()
                    elif resp is not None:
                        st.error(error_detail(resp))

    with tab_manage:
        flt = st.selectbox(
            "Filtrar por tipo",
            ["todas", "post", "evento"],
            format_func=lambda t: {"todas": "Todas", "post": "📝 Posts",
                                   "evento": "📅 Eventos"}[t],
        )
        resp = make_request("GET", "/feed")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return
        items = resp.json()
        if flt != "todas":
            items = [i for i in items if i.get("type") == flt]
        if not items:
            st.info("Nenhuma publicação encontrada.")
            return
        for item in items:
            render_feed_card(item)


def render_feed_card(item):
    label, emoji, pill_cls = FEED_TYPE_META.get(
        item.get("type", "post"), ("Publicação", "📝", "pill-post")
    )
    created = (item.get("created_at") or "")[:10]
    image_url = item.get("image_url")

    with st.container(border=True):
        if image_url:
            st.image(image_url, use_container_width=True)
        st.markdown(
            f'<span class="pill {pill_cls}">{emoji} {label}</span>'
            f'<div class="card-title">{item.get("title","(sem título)")}</div>'
            f'<div class="card-meta">Publicado em {created or "—"}</div>'
            f'<div class="card-body">{item.get("description","")}</div>',
            unsafe_allow_html=True,
        )

        with st.expander("✏️ Editar / remover"):
            with st.form(f"edit_feed_{item['id']}"):
                new_type = st.radio(
                    "Tipo",
                    FEED_TYPES,
                    index=FEED_TYPES.index(item["type"]) if item.get("type") in FEED_TYPES else 0,
                    horizontal=True,
                    format_func=lambda t: f"{FEED_TYPE_META[t][1]} {FEED_TYPE_META[t][0]}",
                    key=f"type_{item['id']}",
                )
                new_title = st.text_input("Título", value=item.get("title", ""))
                new_desc = st.text_area("Descrição", value=item.get("description", ""), height=110)
                new_img_url = st.text_input("URL da imagem", value=item.get("image_url") or "")
                new_img_path = st.text_input("Caminho da imagem", value=item.get("image_path") or "")
                c1, c2 = st.columns(2)
                save = c1.form_submit_button("💾 Salvar alterações")
                delete = c2.form_submit_button("🗑️ Remover")

            if save:
                payload = {
                    "title": new_title,
                    "type": new_type,
                    "description": new_desc,
                    "image_url": new_img_url or None,
                    "image_path": new_img_path or None,
                    "created_at": item.get("created_at"),  # preserva a data original
                }
                r = make_request("PUT", f"/feed/{item['id']}", payload)
                if r is not None and r.status_code == 200:
                    st.success("Publicação atualizada!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))
            if delete:
                r = make_request("DELETE", f"/feed/{item['id']}")
                if r is not None and r.status_code == 200:
                    st.success("Publicação removida!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))


# ----------------------------------------------------------------------------
# Oportunidades de voluntariado
# ----------------------------------------------------------------------------
def oportunidades_section():
    st.subheader("🤝 Oportunidades de Voluntariado")
    st.caption("Vagas de voluntariado exibidas no app (coleção oportunidades).")

    tab_create, tab_manage = st.tabs(["➕ Nova oportunidade", "🗂️ Gerenciar"])

    with tab_create:
        with st.form("create_op", clear_on_submit=True):
            titulo = st.text_input("Título")
            descricao = st.text_area("Descrição", height=120)
            c1, c2 = st.columns(2)
            local = c1.text_input("Local")
            horario = c2.text_input("Horário", placeholder="ex: Sáb 9h–12h")
            c3, c4 = st.columns(2)
            vagas_totais = c3.number_input("Vagas totais", min_value=1, value=10)
            vagas_preenchidas = c4.number_input("Vagas preenchidas", min_value=0, value=0)
            imagem_url = st.text_input("URL da imagem (opcional)")
            ativo = st.checkbox("Ativa", value=True)
            if st.form_submit_button("Publicar oportunidade"):
                if not (titulo and descricao and local and horario):
                    st.error("Preencha título, descrição, local e horário.")
                else:
                    payload = {
                        "titulo": titulo,
                        "descricao": descricao,
                        "local": local,
                        "horario": horario,
                        "vagas_totais": int(vagas_totais),
                        "vagas_preenchidas": int(vagas_preenchidas),
                        "imagem_url": imagem_url or None,
                        "ativo": ativo,
                    }
                    resp = make_request("POST", "/oportunidades", payload)
                    if resp is not None and resp.status_code == 200:
                        st.success("Oportunidade criada com sucesso!")
                        st.rerun()
                    elif resp is not None:
                        st.error(error_detail(resp))

    with tab_manage:
        resp = make_request("GET", "/oportunidades")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return
        ops = resp.json()
        if not isinstance(ops, list) or not ops:
            st.info("Nenhuma oportunidade cadastrada ainda.")
            return
        for op in ops:
            render_oportunidade_card(op)


def render_oportunidade_card(op):
    ativo = op.get("ativo", True)
    vagas_t = op.get("vagas_totais", 0) or 0
    vagas_p = op.get("vagas_preenchidas", 0) or 0
    imagem = op.get("imagem_url")

    with st.container(border=True):
        if imagem:
            st.image(imagem, use_container_width=True)
        status_pill = (
            '<span class="pill pill-vaga">🤝 Vaga aberta</span>'
            if ativo
            else '<span class="pill pill-inactive">Inativa</span>'
        )
        st.markdown(
            f'{status_pill}'
            f'<div class="card-title">{op.get("titulo","(sem título)")}</div>'
            f'<div class="card-meta">📍 {op.get("local","")} &nbsp;·&nbsp; 🕒 {op.get("horario","")}</div>'
            f'<div class="card-body">{op.get("descricao","")}</div>'
            f'<div style="margin-top:8px;"><span style="display:inline-block;background:#F4F6FA;'
            f'color:#475569;padding:5px 12px;border-radius:10px;font-size:.82rem;font-weight:600;">'
            f'👥 {vagas_p}/{vagas_t} vagas preenchidas</span></div>',
            unsafe_allow_html=True,
        )

        with st.expander("✏️ Editar / remover"):
            with st.form(f"edit_op_{op['id']}"):
                e_titulo = st.text_input("Título", value=op.get("titulo", ""))
                e_desc = st.text_area("Descrição", value=op.get("descricao", ""), height=110)
                ec1, ec2 = st.columns(2)
                e_local = ec1.text_input("Local", value=op.get("local", ""))
                e_horario = ec2.text_input("Horário", value=op.get("horario", ""))
                ec3, ec4 = st.columns(2)
                e_vt = ec3.number_input("Vagas totais", min_value=0, value=int(vagas_t), key=f"vt_{op['id']}")
                e_vp = ec4.number_input("Vagas preenchidas", min_value=0, value=int(vagas_p), key=f"vp_{op['id']}")
                e_img = st.text_input("URL da imagem", value=op.get("imagem_url") or "")
                e_ativo = st.checkbox("Ativa", value=ativo, key=f"at_{op['id']}")
                oc1, oc2 = st.columns(2)
                save = oc1.form_submit_button("💾 Salvar alterações")
                delete = oc2.form_submit_button("🗑️ Remover")

            if save:
                payload = {
                    "titulo": e_titulo,
                    "descricao": e_desc,
                    "local": e_local,
                    "horario": e_horario,
                    "vagas_totais": int(e_vt),
                    "vagas_preenchidas": int(e_vp),
                    "imagem_url": e_img or None,
                    "ativo": e_ativo,
                }
                r = make_request("PUT", f"/oportunidades/{op['id']}", payload)
                if r is not None and r.status_code == 200:
                    st.success("Oportunidade atualizada!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))
            if delete:
                r = make_request("DELETE", f"/oportunidades/{op['id']}")
                if r is not None and r.status_code == 200:
                    st.success("Oportunidade removida!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))


# ----------------------------------------------------------------------------
# Administradores
# ----------------------------------------------------------------------------
def admins_page():
    st.subheader("👥 Administradores")
    if st.session_state.get("admin_role") != "master":
        st.warning("Acesso restrito. Apenas o administrador principal pode gerenciar admins.")
        return

    tab_create, tab_manage = st.tabs(["➕ Novo admin", "🗂️ Gerenciar"])

    with tab_create:
        with st.form("create_admin", clear_on_submit=True):
            name = st.text_input("Nome")
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("Criar administrador"):
                resp = make_request("POST", "/admin/create",
                                    {"name": name, "email": email, "password": password})
                if resp is not None and resp.status_code == 200:
                    st.success("Administrador criado!")
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
                    f'<div class="card-meta">{admin["email"]} · {status}</div>',
                    unsafe_allow_html=True,
                )
                if admin["role"] != "master" and admin["is_active"]:
                    if c2.button("Desativar", key=f"deact_{admin['id']}"):
                        r = make_request("DELETE", f"/admin/{admin['id']}")
                        if r is not None and r.status_code == 200:
                            st.success("Admin desativado!")
                            st.rerun()
                        elif r is not None:
                            st.error(error_detail(r))


# ----------------------------------------------------------------------------
# Dashboard
# ----------------------------------------------------------------------------
def main_dashboard():
    role_label = ("Administrador Principal"
                  if st.session_state["admin_role"] == "master" else "Administrador")
    st.markdown(
        f'<div class="hero"><h1>Olá, {st.session_state["admin_name"]} 👋</h1>'
        f'<p>{role_label} · Painel de gestão DoaNet</p></div>',
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.markdown("### ❤️ DoaNet")
        st.caption(st.session_state.get("admin_email", ""))
        st.markdown("---")
        menu = st.radio(
            "Navegação",
            ["📋 Publicações", "🤝 Oportunidades", "👥 Administradores", "ℹ️ Sobre"],
            label_visibility="collapsed",
        )
        st.markdown("---")
        if st.button("🚪 Sair", use_container_width=True):
            for key in _defaults:
                st.session_state[key] = _defaults[key]
            st.rerun()

    if menu == "📋 Publicações":
        publicacoes_section()
    elif menu == "🤝 Oportunidades":
        oportunidades_section()
    elif menu == "👥 Administradores":
        admins_page()
    else:
        st.subheader("ℹ️ Sobre")
        st.write("Sistema de gerenciamento da ONG — publique posts, eventos e oportunidades de voluntariado.")


# ----------------------------------------------------------------------------
# Roteamento
# ----------------------------------------------------------------------------
inject_css()
if not st.session_state.get("logged_in"):
    login_page()
else:
    main_dashboard()
