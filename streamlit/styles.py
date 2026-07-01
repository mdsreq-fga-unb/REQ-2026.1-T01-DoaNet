"""Estilo do painel — alinhado à identidade do app (azul #0088FF sobre fundo
claro, cards Material e tipografia Inter)."""
import streamlit as st


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
