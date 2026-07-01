"""Estilo do painel — alinhado à identidade do app (azul #0088FF sobre fundo
claro, cards Material e tipografia Inter)."""
import streamlit as st


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --brand:      #0088FF;
            --brand-2:    #3AA0FF;
            --brand-dark: #0070D6;
            --ink:        #1F2937;
            --muted:      #6B7280;
            --canvas:     #F4F7FB;
            --line:       #E6EBF2;
            --card:       #FFFFFF;
        }

        /* ---- Tipografia responsiva base ---- */
        html { font-size: clamp(14px, 0.95vw + 10px, 16px); }
        html, body, [class*="css"], button, input, textarea, select {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .stApp { background: var(--canvas); }
        [data-testid="stHeader"] { background: transparent; }
        .block-container {
            padding-top: 1.75rem;
            padding-left: clamp(1rem, 3vw, 2.5rem);
            padding-right: clamp(1rem, 3vw, 2.5rem);
            max-width: 1120px;
        }

        /* ---- Hero ---- */
        .hero {
            background: linear-gradient(135deg, #0088FF 0%, #2E97F7 100%);
            padding: clamp(18px, 2.5vh, 28px) clamp(20px, 3vw, 34px);
            border-radius: 18px; color: #fff;
            box-shadow: 0 8px 24px rgba(16,24,40,.10);
            margin-bottom: 22px;
        }
        .hero h1 {
            color: #fff;
            font-size: clamp(1.2rem, 2vw, 1.55rem);
            font-weight: 800; margin: 0; letter-spacing: -.4px;
        }
        .hero p { color: rgba(255,255,255,.92); margin: 6px 0 0; font-size: clamp(.82rem, 1.2vw, .95rem); }

        /* ---- Brand / Auth ---- */
        .auth-badge {
            width: 60px; height: 60px; border-radius: 16px; margin: 0 auto 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px; font-weight: 800; color: #fff;
            background: #0088FF; box-shadow: 0 6px 16px rgba(16,24,40,.12);
        }
        .side-brand {
            display: flex; align-items: center; gap: 11px;
            padding: 4px 2px 6px;
        }
        .side-logo {
            width: clamp(34px, 3vw, 40px);
            height: clamp(34px, 3vw, 40px);
            border-radius: 11px;
            background: #0088FF; color: #fff;
            display: flex; align-items: center; justify-content: center;
            font-weight: 800;
            font-size: clamp(18px, 1.8vw, 22px);
            flex-shrink: 0;
        }
        .side-name {
            font-weight: 800;
            font-size: clamp(1.1rem, 1.5vw, 1.3rem);
            color: #0F172A; letter-spacing: -.3px;
        }
        .side-email {
            font-size: clamp(0.78rem, 1vw, 0.88rem);
            color: var(--muted);
            margin: 2px 0 10px 0;
            display: block;
            word-break: break-all;
        }

        /* ---- Pills ---- */
        .pill {
            display: inline-flex; align-items: center; gap: 5px;
            padding: 3px 11px; border-radius: 999px;
            font-size: clamp(.66rem, .9vw, .72rem);
            font-weight: 700; letter-spacing: .5px; text-transform: uppercase;
        }
        .pill-post     { background: #E7F0FF; color: #2563EB; }
        .pill-evento   { background: #EFEAFE; color: #7C3AED; }
        .pill-vaga     { background: #E7F9EE; color: #16A34A; }
        .pill-despesa  { background: #FFECEF; color: #E11D48; }
        .pill-inactive { background: #F1F3F7; color: #94A3B8; }
        .dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }

        /* ---- Card typography ---- */
        .card-title {
            font-size: clamp(.98rem, 1.3vw, 1.1rem);
            font-weight: 700; color: #1F2330; margin: 7px 0 3px;
        }
        .card-meta  { color: #6B7280; font-size: clamp(.78rem, 1vw, .86rem); margin-bottom: 6px; }
        .card-body  { color: #374151; font-size: clamp(.88rem, 1.1vw, .95rem); line-height: 1.55; }
        .vagas-badge {
            display: inline-block; background: #EEF3FA; color: #475569;
            padding: 5px 13px; border-radius: 10px;
            font-size: clamp(.78rem, 1vw, .85rem); font-weight: 600;
        }

        /* ---- Cards (st.container border=True) ---- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 14px;
            border: 1px solid var(--line) !important;
            background: var(--card);
            box-shadow: 0 1px 4px rgba(16,24,40,.06);
        }
        [data-testid="stForm"] {
            border: 1px solid var(--line); border-radius: 14px;
            background: var(--card);
            box-shadow: 0 1px 3px rgba(16,24,40,.05);
        }

        /* ---- Buttons ---- */
        .stButton > button {
            border-radius: 10px; font-weight: 600;
            font-size: clamp(.85rem, 1vw, .95rem);
            border: 1px solid var(--line);
            background: #fff; color: #374151;
            transition: all .15s ease;
        }
        .stButton > button:hover {
            border-color: var(--brand); color: var(--brand);
            transform: translateY(-1px);
        }
        .stButton > button[kind="primary"],
        [data-testid="stFormSubmitButton"] button {
            background: #0088FF; color: #fff; border: none;
            border-radius: 10px; font-weight: 700;
            font-size: clamp(.88rem, 1.1vw, .98rem);
            padding: .55rem 1.4rem; width: 100%;
            box-shadow: 0 1px 2px rgba(16,24,40,.10);
        }
        .stButton > button[kind="primary"]:hover,
        [data-testid="stFormSubmitButton"] button:hover {
            background: #0070D6;
            box-shadow: 0 4px 12px rgba(16,24,40,.14);
            transform: translateY(-1px);
        }

        /* ---- Inputs ---- */
        [data-baseweb="input"],
        [data-baseweb="textarea"],
        [data-baseweb="select"] > div {
            border: 1px solid #D5DCE6 !important;
            border-radius: 10px !important;
            background: #fff !important;
            font-size: clamp(.88rem, 1vw, .95rem) !important;
        }
        /* base-input é o elemento interno — só herda fundo/fonte, sem borda própria */
        [data-baseweb="base-input"] {
            background: transparent !important;
            border: none !important;
            font-size: clamp(.88rem, 1vw, .95rem) !important;
        }
        [data-baseweb="input"]:focus-within,
        [data-baseweb="textarea"]:focus-within,
        [data-baseweb="select"] > div:focus-within {
            border-color: #0088FF !important;
            box-shadow: 0 0 0 3px rgba(0,136,255,.12) !important;
        }
        [data-testid="stTextInput"] label,
        [data-testid="stTextArea"] label,
        [data-testid="stNumberInput"] label,
        [data-testid="stSelectbox"] label,
        [data-testid="stDateInput"] label {
            font-size: clamp(.82rem, 1vw, .9rem) !important;
            font-weight: 600; color: #374151;
        }
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stNumberInput"] input,
        [data-testid="stDateInput"] input { color: #1F2937; }
        [data-testid="stFileUploaderDropzone"] {
            border: 1px dashed #C9D2DE !important;
            border-radius: 10px; background: #fff;
        }

        /* ---- Metrics ---- */
        [data-testid="stMetric"] {
            background: #fff; border: 1px solid var(--line);
            border-radius: 14px; padding: 14px 18px;
            box-shadow: 0 2px 10px rgba(16,40,80,.04);
        }
        [data-testid="stMetricLabel"] { font-size: clamp(.8rem, 1vw, .9rem) !important; }
        [data-testid="stMetricValue"] { font-size: clamp(1.4rem, 2.5vw, 2rem) !important; }

        /* ---- Subheaders ---- */
        [data-testid="stHeadingWithActionElements"] h2,
        .stSubheader {
            font-size: clamp(1.1rem, 1.8vw, 1.4rem) !important;
            font-weight: 700; color: #0F172A;
        }

        /* ---- Caption / info text ---- */
        [data-testid="stCaptionContainer"] p {
            font-size: clamp(.78rem, 1vw, .86rem) !important;
            color: var(--muted);
        }

        /* ======================================================
           Sidebar
           ====================================================== */
        section[data-testid="stSidebar"] {
            background: #fff;
            border-right: 1px solid #EAEEF3;
            min-width: 220px;
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.25rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* Navegação lateral */
        section[data-testid="stSidebar"] div[role="radiogroup"] {
            display: flex; flex-direction: column; gap: 3px;
            background: transparent; padding: 0; border-radius: 0;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            margin: 0 !important;
            padding: clamp(10px, 1.2vh, 13px) 14px;
            border-radius: 10px; color: #4B5563;
            font-weight: 500;
            transition: all .15s ease;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
            display: none;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label > div:last-child {
            font-size: clamp(0.95rem, 1.2vw, 1.05rem) !important;
            font-weight: 500; color: inherit !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: rgba(0,136,255,.07); color: var(--brand);
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background: rgba(0,136,255,.12); color: var(--brand);
            font-weight: 700;
            box-shadow: inset 3px 0 0 var(--brand);
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) > div:last-child {
            font-weight: 700 !important;
        }

        /* "Sair" button na sidebar */
        section[data-testid="stSidebar"] .stButton > button {
            font-size: clamp(.88rem, 1vw, .96rem);
            color: #6B7280; border-color: #E2E8F0;
            margin-top: 4px;
        }
        section[data-testid="stSidebar"] .stButton > button:hover {
            color: #E11D48; border-color: #E11D48;
        }

        /* ======================================================
           Segmented control — radio horizontal (conteúdo)
           ====================================================== */
        div[role="radiogroup"] {
            display: inline-flex; flex-wrap: wrap; gap: 4px;
            background: #EEF2F7; padding: 5px; border-radius: 12px;
        }
        div[role="radiogroup"] label {
            margin: 0 !important; padding: 7px 18px; border-radius: 9px;
            cursor: pointer; transition: all .15s ease; color: #6B7280; font-weight: 600;
        }
        div[role="radiogroup"] label > div:first-child { display: none; }
        div[role="radiogroup"] label > div:last-child {
            color: inherit !important; font-size: clamp(.84rem, 1vw, .92rem);
        }
        div[role="radiogroup"] label:hover { color: var(--brand); }
        div[role="radiogroup"] label:has(input:checked) {
            background: #fff; color: var(--brand);
            box-shadow: 0 2px 8px rgba(16,40,80,.10);
        }

        /* ======================================================
           Tabs
           ====================================================== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px; background: #EEF2F7; padding: 5px; border-radius: 12px;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 9px; padding: 8px 20px;
            font-weight: 600; font-size: clamp(.86rem, 1.1vw, .95rem);
            color: #6B7280;
        }
        .stTabs [data-baseweb="tab"] p { color: inherit !important; font-weight: 600; }
        .stTabs [data-baseweb="tab"]:hover { color: var(--brand); }
        .stTabs [aria-selected="true"] {
            background: #fff; color: var(--brand) !important;
            box-shadow: 0 2px 8px rgba(16,40,80,.10);
        }
        .stTabs [data-baseweb="tab-highlight"],
        .stTabs [data-baseweb="tab-border"] { display: none; }

        /* Expanders */
        [data-testid="stExpander"] {
            border: 1px solid var(--line) !important;
            border-radius: 10px !important;
            background: #FAFBFD;
        }
        [data-testid="stExpander"] summary {
            font-size: clamp(.86rem, 1vw, .93rem) !important;
            font-weight: 600; color: var(--brand);
        }

        /* Toast / alert */
        [data-testid="stToast"] { font-size: clamp(.85rem, 1vw, .92rem); }

        #MainMenu, footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )
