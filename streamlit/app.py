import streamlit as st
import requests
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000"

# A coleção org_feed guarda 2 tipos de publicação: "post" e "evento".
# Ambos compartilham os mesmos campos (title, type, description, image_url, image_path).
FEED_TYPES = ["post", "evento"]
FEED_TYPE_META = {
    "post": ("Post", "pill-post"),
    "evento": ("Evento", "pill-evento"),
}

st.set_page_config(
    page_title="DoaNet · Admin",
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
    "admin_org_id": None,
}
for _k, _v in _defaults.items():
    st.session_state.setdefault(_k, _v)


# ----------------------------------------------------------------------------
# Estilo — alinhado à identidade do app (azul #0088FF sobre fundo claro,
# cards Material e tipografia Inter).
# ----------------------------------------------------------------------------
def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --brand:#0088FF;
            --brand-2:#3AA0FF;
            --brand-dark:#0070D6;
            --ink:#1F2937;
            --muted:#6B7280;
            --canvas:#F4F7FB;
            --line:#E6EBF2;
        }

        html, body, [class*="css"], button, input, textarea, select {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .stApp { background: var(--canvas); }
        [data-testid="stHeader"] { background: transparent; }
        .block-container { padding-top: 2rem; max-width: 1080px; }

        /* ---- Hero ---- */
        .hero {
            background: linear-gradient(135deg, #0088FF 0%, #2E97F7 100%);
            padding: 26px 32px; border-radius: 18px; color: #fff;
            box-shadow: 0 8px 24px rgba(16,24,40,.10);
            margin-bottom: 22px;
        }
        .hero h1 { color:#fff; font-size:1.55rem; font-weight:800; margin:0; letter-spacing:-.4px; }
        .hero p  { color:rgba(255,255,255,.92); margin:6px 0 0; font-size:.95rem; }

        /* ---- Brand / Auth ---- */
        .auth-badge {
            width:60px; height:60px; border-radius:16px; margin:0 auto 14px;
            display:flex; align-items:center; justify-content:center;
            font-size:24px; font-weight:800; color:#fff; letter-spacing:.5px;
            background:#0088FF;
            box-shadow:0 6px 16px rgba(16,24,40,.12);
        }
        .side-brand { display:flex; align-items:center; gap:10px; padding:2px 2px 4px; }
        .side-logo {
            width:34px; height:34px; border-radius:10px;
            background:#0088FF; color:#fff;
            display:flex; align-items:center; justify-content:center;
            font-weight:800; font-size:18px;
        }
        .side-name { font-weight:800; font-size:1.15rem; color:#0F172A; letter-spacing:-.3px; }

        /* ---- Pills ---- */
        .pill { display:inline-flex; align-items:center; gap:6px; padding:3px 12px;
            border-radius:999px; font-size:.68rem; font-weight:700;
            letter-spacing:.5px; text-transform:uppercase; }
        .pill-post     { background:#E7F0FF; color:#2563EB; }
        .pill-evento   { background:#EFEAFE; color:#7C3AED; }
        .pill-vaga     { background:#E7F9EE; color:#16A34A; }
        .pill-despesa  { background:#FFECEF; color:#E11D48; }
        .pill-inactive { background:#F1F3F7; color:#94A3B8; }
        .dot { width:8px; height:8px; border-radius:50%; display:inline-block; }

        .card-title { font-size:1.06rem; font-weight:700; color:#1F2330; margin:6px 0 2px; }
        .card-meta  { color:#6B7280; font-size:.83rem; margin-bottom:6px; }
        .card-body  { color:#374151; font-size:.92rem; line-height:1.5; }
        .vagas-badge { display:inline-block; background:#EEF3FA; color:#475569;
            padding:5px 12px; border-radius:10px; font-size:.82rem; font-weight:600; }

        /* ---- Cards (st.container border=True) ---- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius:14px;
            box-shadow:0 1px 3px rgba(16,24,40,.06);
        }
        [data-testid="stForm"] {
            border:1px solid var(--line); border-radius:14px;
            box-shadow:0 1px 3px rgba(16,24,40,.06);
        }

        /* ---- Buttons ---- */
        .stButton > button {
            border-radius:10px; font-weight:600; border:1px solid var(--line);
            background:#fff; color:#374151; transition:all .15s ease;
        }
        .stButton > button:hover { border-color:var(--brand); color:var(--brand); transform:translateY(-1px); }
        .stButton > button[kind="primary"],
        [data-testid="stFormSubmitButton"] button {
            background:#0088FF; color:#fff; border:none;
            border-radius:10px; font-weight:700; padding:.55rem 1.4rem; width:100%;
            box-shadow:0 1px 2px rgba(16,24,40,.10);
        }
        .stButton > button[kind="primary"]:hover,
        [data-testid="stFormSubmitButton"] button:hover {
            background:#0070D6; box-shadow:0 4px 12px rgba(16,24,40,.14); transform:translateY(-1px);
        }

        /* ---- Inputs (contorno visível sobre fundo branco) ---- */
        [data-baseweb="input"],
        [data-baseweb="base-input"],
        [data-baseweb="textarea"],
        [data-baseweb="select"] > div {
            border:1px solid #D5DCE6 !important;
            border-radius:10px !important;
            background:#fff !important;
        }
        [data-baseweb="input"]:focus-within,
        [data-baseweb="textarea"]:focus-within,
        [data-baseweb="select"] > div:focus-within {
            border-color:#0088FF !important;
            box-shadow:none !important;
        }
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stNumberInput"] input,
        [data-testid="stDateInput"] input { color:#1F2937; }
        [data-testid="stFileUploaderDropzone"] {
            border:1px dashed #C9D2DE !important; border-radius:10px; background:#fff;
        }

        /* ---- Metrics como cartões ---- */
        [data-testid="stMetric"] {
            background:#fff; border:1px solid var(--line); border-radius:14px;
            padding:14px 18px; box-shadow:0 2px 10px rgba(16,40,80,.04);
        }

        /* ---- Sidebar ---- */
        section[data-testid="stSidebar"] { background:#fff; border-right:1px solid #EAEEF3; }

        /* ====================================================================
           Barras de opções (radios) — visual estilizado
           Base: segmented control (usado nas áreas de conteúdo).
           Override do sidebar: menu de navegação vertical.
           O circulo nativo é ocultado; o clique continua no <label>.
           ==================================================================== */
        div[role="radiogroup"] {
            display:inline-flex; flex-wrap:wrap; gap:4px;
            background:#EEF2F7; padding:5px; border-radius:12px;
        }
        div[role="radiogroup"] label {
            margin:0 !important; padding:7px 18px; border-radius:9px;
            cursor:pointer; transition:all .15s ease; color:#6B7280; font-weight:600;
        }
        div[role="radiogroup"] label > div:first-child { display:none; }
        div[role="radiogroup"] label > div:last-child { color:inherit !important; font-size:.9rem; }
        div[role="radiogroup"] label:hover { color:var(--brand); }
        div[role="radiogroup"] label:has(input:checked) {
            background:#fff; color:var(--brand);
            box-shadow:0 2px 8px rgba(16,40,80,.10);
        }

        /* Sidebar: navegação vertical */
        section[data-testid="stSidebar"] div[role="radiogroup"] {
            display:flex; flex-direction:column; gap:4px;
            background:transparent; padding:0; border-radius:0;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            padding:11px 14px; border-radius:10px; color:#4B5563;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label > div:last-child { font-size:.95rem; }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background:rgba(0,136,255,.07); color:var(--brand);
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background:rgba(0,136,255,.12); color:var(--brand);
            box-shadow:inset 3px 0 0 var(--brand);
        }

        /* ---- Tabs (mesmo visual segmentado) ---- */
        .stTabs [data-baseweb="tab-list"] {
            gap:4px; background:#EEF2F7; padding:5px; border-radius:12px;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius:9px; padding:8px 18px; font-weight:600; color:#6B7280;
        }
        .stTabs [data-baseweb="tab"] p { color:inherit !important; font-weight:600; }
        .stTabs [data-baseweb="tab"]:hover { color:var(--brand); }
        .stTabs [aria-selected="true"] {
            background:#fff; color:var(--brand) !important;
            box-shadow:0 2px 8px rgba(16,40,80,.10);
        }
        .stTabs [data-baseweb="tab-highlight"],
        .stTabs [data-baseweb="tab-border"] { display:none; }

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
            '<div class="auth-badge">D</div>'
            '<h2 style="text-align:center;margin:0;">DoaNet</h2>'
            '<p style="text-align:center;color:#6B7280;margin:.2rem 0 1.4rem;">'
            'Painel do Administrador</p>',
            unsafe_allow_html=True,
        )

        has_admins = check_first_admin()
        if has_admins is None:
            st.error(f"Backend indisponível em {BACKEND_URL}. Inicie o servidor e recarregue.")
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
                    st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}).")
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
                        admin_org_id=admin.get("org_id"),
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
                    st.error(f"Não foi possível conectar ao backend ({BACKEND_URL}).")
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
    st.subheader("Publicações")
    st.caption("Posts e eventos do feed. A imagem é enviada por upload (vai para o GCS).")

    tab_create, tab_manage = st.tabs(["Nova publicação", "Gerenciar"])

    with tab_create:
        # Fora do form para que os campos de evento apareçam/sumam ao trocar o tipo.
        ptype = st.radio(
            "Tipo de publicação",
            FEED_TYPES,
            horizontal=True,
            format_func=lambda t: FEED_TYPE_META[t][0],
            key="new_feed_type",
        )
        with st.form("create_feed", clear_on_submit=True):
            title = st.text_input("Título")
            description = st.text_area("Descrição", height=130)
            image = st.file_uploader("Imagem (opcional)", type=["png", "jpg", "jpeg", "webp"])
            if ptype == "evento":
                st.markdown("**Dados do evento** (obrigatórios):")
                ec1, ec2 = st.columns(2)
                event_location = ec1.text_input("Local do evento")
                event_date = ec2.text_input("Data do evento", placeholder="ex: 2026-06-20")
                event_url = st.text_input("Link do evento (URL)")
            else:
                event_location = event_date = event_url = ""

            if st.form_submit_button("Publicar"):
                if not (title and description):
                    st.error("Preencha título e descrição.")
                elif ptype == "evento" and not (event_location and event_date and event_url):
                    st.error("Eventos exigem local, data e link.")
                else:
                    data = {"title": title, "description": description, "post_type": ptype}
                    if ptype == "evento":
                        data["event_location"] = event_location
                        data["event_date"] = event_date
                        data["event_url"] = event_url
                    files = None
                    if image is not None:
                        files = {"image": (image.name, image.getvalue(), image.type)}
                    resp = make_multipart_request("POST", "/feed", data=data, files=files)
                    ok, msg = feed_result_ok(resp)
                    if ok:
                        st.success("Publicação criada com sucesso!")
                        st.rerun()
                    elif resp is not None:
                        st.error(msg)

    with tab_manage:
        flt = st.selectbox(
            "Filtrar por tipo",
            ["todas", "post", "evento"],
            format_func=lambda t: {"todas": "Todas", "post": "Posts",
                                   "evento": "Eventos"}[t],
        )
        resp = make_request("GET", "/feed")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return
        items = resp.json()
        if not isinstance(items, list):
            st.error(items.get("error", "Resposta inesperada do servidor")
                     if isinstance(items, dict) else "Resposta inesperada do servidor")
            return
        if flt != "todas":
            items = [i for i in items if i.get("type") == flt]
        if not items:
            st.info("Nenhuma publicação encontrada.")
            return
        for item in items:
            render_feed_card(item)


def render_feed_card(item):
    label, pill_cls = FEED_TYPE_META.get(
        item.get("type", "post"), ("Publicação", "pill-post")
    )
    image_url = item.get("image_url")
    is_evento = item.get("type") == "evento"

    with st.container(border=True):
        if image_url:
            st.image(image_url, use_container_width=True)

        event_meta = ""
        if is_evento:
            partes = []
            if item.get("event_date"):
                partes.append(item["event_date"])
            if item.get("event_location"):
                partes.append(item["event_location"])
            event_meta = " &nbsp;·&nbsp; ".join(partes)

        st.markdown(
            f'<span class="pill {pill_cls}">{label}</span>'
            f'<div class="card-title">{item.get("title","(sem título)")}</div>'
            + (f'<div class="card-meta">{event_meta}</div>' if event_meta else '')
            + f'<div class="card-body">{item.get("description","")}</div>'
            + (f'<div class="card-meta" style="margin-top:6px;">'
               f'<a href="{item.get("event_url")}" target="_blank">{item.get("event_url")}</a></div>'
               if is_evento and item.get("event_url") else ''),
            unsafe_allow_html=True,
        )

        with st.expander("Editar / remover"):
            # Fora do form para que os campos de evento apareçam/sumam ao trocar o tipo.
            new_type = st.radio(
                "Tipo",
                FEED_TYPES,
                index=FEED_TYPES.index(item["type"]) if item.get("type") in FEED_TYPES else 0,
                horizontal=True,
                format_func=lambda t: FEED_TYPE_META[t][0],
                key=f"type_{item['id']}",
            )
            with st.form(f"edit_feed_{item['id']}"):
                new_title = st.text_input("Título", value=item.get("title", ""))
                new_desc = st.text_area("Descrição", value=item.get("description", ""), height=110)
                new_image = st.file_uploader(
                    "Trocar imagem (opcional — mantém a atual se vazio)",
                    type=["png", "jpg", "jpeg", "webp"], key=f"img_{item['id']}",
                )
                if new_type == "evento":
                    st.caption("Dados do evento (obrigatórios):")
                    ec1, ec2 = st.columns(2)
                    new_loc = ec1.text_input("Local", value=item.get("event_location") or "", key=f"loc_{item['id']}")
                    new_date = ec2.text_input("Data", value=item.get("event_date") or "", key=f"date_{item['id']}")
                    new_url = st.text_input("Link (URL)", value=item.get("event_url") or "", key=f"url_{item['id']}")
                else:
                    new_loc = new_date = new_url = ""
                c1, c2 = st.columns(2)
                save = c1.form_submit_button("Salvar alterações")
                delete = c2.form_submit_button("Remover")

            if save:
                if new_type == "evento" and not (new_loc and new_date and new_url):
                    st.error("Eventos exigem local, data e link.")
                else:
                    data = {"title": new_title, "description": new_desc, "post_type": new_type}
                    if new_type == "evento":
                        data["event_location"] = new_loc
                        data["event_date"] = new_date
                        data["event_url"] = new_url
                    files = None
                    if new_image is not None:
                        files = {"image": (new_image.name, new_image.getvalue(), new_image.type)}
                    r = make_multipart_request("PUT", f"/feed/{item['id']}", data=data, files=files)
                    ok, msg = feed_result_ok(r)
                    if ok:
                        st.success("Publicação atualizada!")
                        st.rerun()
                    elif r is not None:
                        st.error(msg)
            if delete:
                r = make_request("DELETE", f"/feed/{item['id']}")
                ok, msg = feed_result_ok(r)
                if ok:
                    st.success("Publicação removida!")
                    st.rerun()
                elif r is not None:
                    st.error(msg)


# ----------------------------------------------------------------------------
# Oportunidades de voluntariado
# ----------------------------------------------------------------------------
def oportunidades_section():
    st.subheader("Oportunidades de Voluntariado")
    st.caption("Vagas de voluntariado exibidas no app (coleção oportunidades).")

    tab_create, tab_manage = st.tabs(["Nova oportunidade", "Gerenciar"])

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
            '<span class="pill pill-vaga">Vaga aberta</span>'
            if ativo
            else '<span class="pill pill-inactive">Inativa</span>'
        )
        st.markdown(
            f'{status_pill}'
            f'<div class="card-title">{op.get("titulo","(sem título)")}</div>'
            f'<div class="card-meta">{op.get("local","")} &nbsp;·&nbsp; {op.get("horario","")}</div>'
            f'<div class="card-body">{op.get("descricao","")}</div>'
            f'<div style="margin-top:8px;"><span class="vagas-badge">'
            f'{vagas_p}/{vagas_t} vagas preenchidas</span></div>',
            unsafe_allow_html=True,
        )

        with st.expander("Editar / remover"):
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
                save = oc1.form_submit_button("Salvar alterações")
                delete = oc2.form_submit_button("Remover")

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

#financeiro
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def financeiro_section():
    st.subheader("Financeiro")
    st.caption("Lance doações externas e despesas. Registros são permanentes e não podem ser editados.")

    if "success_msg" in st.session_state:
        st.success(st.session_state["success_msg"])
        del st.session_state["success_msg"]

    aba_opcoes = ["Lançar Doação Externa", "Lançar Despesa", "Histórico"]
    if "financeiro_aba_ativa" not in st.session_state:
        st.session_state["financeiro_aba_ativa"] = aba_opcoes[0]

    aba_selecionada = st.radio(
        "Seção financeira",
        aba_opcoes,
        horizontal=True,
        key="financeiro_aba_ativa",
        label_visibility="collapsed",
    )

    # doacao externa
    if aba_selecionada == "Lançar Doação Externa":
        with st.form("form_doacao", clear_on_submit=True):
            col1, col2 = st.columns(2)
            valor = col1.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f")
            data = col2.date_input("Data da doação")
            descricao = st.text_area("Descrição", placeholder="ex: Doação em dinheiro recebida no evento de Maio")

            if st.form_submit_button("Confirmar doação"):
                if not descricao:
                    st.error("Preencha a descrição.")
                else:
                    st.session_state["pending_doacao"] = {
                        "valor": valor,
                        "data": data.isoformat(),
                        "descricao": descricao,
                    }

        pending = st.session_state.get("pending_doacao")
        if pending:
            st.warning(
                f"Tem certeza que deseja registrar a doação de "
                f"**R$ {pending['valor']:,.2f}** — \"{pending['descricao']}\"?\n\n"
                "Essa ação não pode ser desfeita."
            )
            c1, c2 = st.columns(2)
            if c1.button("Sim, confirmar doação", type="primary", use_container_width=True, key="btn_confirma_doacao"):
                resp = make_request("POST", "/transparencia/doacao-externa", data=pending)
                if resp is not None and resp.status_code == 200:
                    del st.session_state["pending_doacao"]
                    st.session_state["success_msg"] = "Doação registrada com sucesso!"
                    st.rerun()
                elif resp is not None:
                    st.error(error_detail(resp))
            if c2.button("Cancelar", use_container_width=True, key="btn_cancela_doacao"):
                del st.session_state["pending_doacao"]
                st.rerun()

   # despesa
    if aba_selecionada == "Lançar Despesa":
        with st.form("form_despesa", clear_on_submit=True):
            col1, col2 = st.columns(2)
            valor = col1.number_input("Valor (R$)", min_value=0.01, step=0.01, format="%.2f", key="valor_despesa")
            data = col2.date_input("Data da despesa", key="data_despesa")
            categoria = st.text_input("Categoria", placeholder="ex: Aluguel, Material, Transporte")

            if st.form_submit_button("Confirmar despesa"):
                if not categoria:
                    st.error("Preencha a categoria.")
                else:
                    st.session_state["pending_despesa"] = {
                        "valor": valor,
                        "data": data.isoformat(),
                        "categoria": categoria,
                    }

        pending = st.session_state.get("pending_despesa")
        if pending:
            st.warning(
                f"Tem certeza que deseja registrar a despesa de "
                f"**R$ {pending['valor']:,.2f}** — \"{pending['categoria']}\"?\n\n"
                "Essa ação não pode ser desfeita."
            )
            c1, c2 = st.columns(2)
            if c1.button("Sim, confirmar despesa", type="primary", use_container_width=True, key="btn_confirma_despesa"):
                resp = make_request("POST", "/transparencia/despesa", data=pending)
                if resp is not None and resp.status_code == 200:
                    del st.session_state["pending_despesa"]
                    st.session_state["success_msg"] = "Despesa registrada com sucesso!"
                    st.rerun()
                elif resp is not None:
                    st.error(error_detail(resp))
            if c2.button("Cancelar", use_container_width=True, key="btn_cancela_despesa"):
                del st.session_state["pending_despesa"]
                st.rerun()

    # historico
    if aba_selecionada == "Histórico":
        resp = make_request("GET", "/transparencia")
        if resp is None:
            return
        if resp.status_code != 200:
            st.error(error_detail(resp))
            return

        records = resp.json()
        if not isinstance(records, list):
            st.error("Resposta inesperada do servidor")
            return
        if not records:
            st.info("Nenhum registro encontrado.")
            return

        total_in = sum(r["valor"] for r in records if r["tipo"] != "despesa")
        total_out = sum(r["valor"] for r in records if r["tipo"] == "despesa")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total arrecadado", formatar_real(total_in))
        c2.metric("Total de despesas", formatar_real(total_out))
        c3.metric("Saldo", formatar_real(total_in - total_out))

        st.divider()

        for r in records:
            render_transparencia_card(r)


def render_transparencia_card(r):
    tipo_meta = {
        "doacao_externa": ("Doação externa", "pill-vaga", "#16A34A"),
        "doacao_interna": ("Doação interna", "pill-post", "#2563EB"),
        "despesa":        ("Despesa",        "pill-despesa", "#E11D48"),
    }
    label, pill_cls, dot_color = tipo_meta.get(r["tipo"], ("Registro", "pill-inactive", "#94A3B8"))
    sinal = "-" if r["tipo"] == "despesa" else "+"
    cor_valor = "#E11D48" if r["tipo"] == "despesa" else "#16A34A"
    data_fmt = r["data"][:10] if r.get("data") else "—"

    with st.container(border=True):
        col_info, col_valor = st.columns([4, 1])
        with col_info:
            st.markdown(
                f'<span class="pill {pill_cls}">'
                f'<span class="dot" style="background:{dot_color};"></span>{label}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<div class="card-title">{r["descricao"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card-meta">{data_fmt}</div>', unsafe_allow_html=True)
        with col_valor:
            st.markdown(
                f'<div style="text-align:right; font-weight:800; font-size:1.1rem; '
                f'color:{cor_valor}; padding-top:8px;">{sinal} {formatar_real(r["valor"])}</div>',
                unsafe_allow_html=True,
            )
# ----------------------------------------------------------------------------
# Administradores
# ----------------------------------------------------------------------------
def admins_page():
    st.subheader("Administradores")
    if st.session_state.get("admin_role") != "master":
        st.warning("Acesso restrito. Apenas o administrador principal pode gerenciar admins.")
        return

    tab_create, tab_manage = st.tabs(["Novo admin", "Gerenciar"])

    with tab_create:
        with st.form("create_admin", clear_on_submit=True):
            name = st.text_input("Nome")
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            org_id = st.text_input("ID da organização", placeholder="ex: move-educa")
            st.caption("O admin só poderá configurar a organização com esse ID.")
            if st.form_submit_button("Criar administrador"):
                if not org_id:
                    st.error("Informe o ID da organização.")
                else:
                    resp = make_request("POST", "/admin/create",
                                    {"name": name, "email": email,
                                     "password": password, "org_id": org_id})
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
                    f'<div class="card-meta">{admin["email"]} · {status}</div>'
                    + (f'<div class="card-meta">{admin["org_id"]}</div>' if admin.get("org_id") else ''),
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

def organizacao_section():
    st.subheader("Minha Organização")

    role = st.session_state.get("admin_role")
    if role == "master":
        org_id = st.text_input("ID da organização a configurar", placeholder="ex: move-educa")
        if not org_id:
            st.info("Informe o ID da organização para carregar ou criar as configurações.")
            return
    else:
        org_id = st.session_state.get("admin_org_id")
        if not org_id:
            st.error("Sua conta não está vinculada a nenhuma organização. Contate o administrador principal.")
            return
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
                r = make_multipart_request("POST", "/orgs", data=data, files=files)
                if r is not None and r.status_code == 200:
                    st.success("Configurações salvas! O app já reflete as mudanças.")
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
        f'<div class="hero"><h1>Olá, {st.session_state["admin_name"]}</h1>'
        f'<p>{role_label} · Painel de gestão DoaNet</p></div>',
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.markdown(
            '<div class="side-brand"><span class="side-logo">D</span>'
            '<span class="side-name">DoaNet</span></div>',
            unsafe_allow_html=True,
        )
        st.caption(st.session_state.get("admin_email", ""))
        st.markdown("---")
        menu = st.radio(
            "Navegação",
            ["Publicações", "Oportunidades", "Financeiro", "Organização", "Administradores", "Sobre"],
            label_visibility="collapsed",
        )
        st.markdown("---")
        if st.button("Sair", use_container_width=True):
            for key in _defaults:
                st.session_state[key] = _defaults[key]
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


# ----------------------------------------------------------------------------
# Roteamento
# ----------------------------------------------------------------------------
inject_css()
if not st.session_state.get("logged_in"):
    login_page()
else:
    main_dashboard()
