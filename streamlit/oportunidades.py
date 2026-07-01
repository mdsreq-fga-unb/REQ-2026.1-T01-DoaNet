"""Oportunidades de voluntariado."""
import streamlit as st

from api import make_request, error_detail
from ui import flash, show_flash


def oportunidades_section():
    st.subheader("Oportunidades de Voluntariado")
    st.caption("Vagas de voluntariado exibidas no app (coleção oportunidades).")
    show_flash()

    tab_create, tab_manage = st.tabs(["Nova oportunidade", "Gerenciar"])

    with tab_create:
        with st.form("create_op", clear_on_submit=True):
            titulo = st.text_input("Título")
            descricao = st.text_area("Descrição", height=120)
            c1, c2 = st.columns(2)
            local = c1.text_input("Local")
            horario = c2.text_input("Horário", placeholder="ex: Sáb 9h–12h")
            link_inscricao = st.text_input("Link de inscrição (URL)")
            if st.form_submit_button("Publicar oportunidade"):
                if not (titulo and descricao and local and horario):
                    st.error("Preencha título, descrição, local e horário.")
                else:
                    payload = {
                        "titulo": titulo,
                        "descricao": descricao,
                        "local": local,
                        "horario": horario,
                        "link_inscricao": link_inscricao or None,
                    }
                    with st.spinner("Publicando..."):
                        resp = make_request("POST", "/oportunidades", payload)
                    if resp is not None and resp.status_code == 200:
                        flash("Oportunidade criada com sucesso!")
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
    link = op.get("link_inscricao")

    with st.container(border=True):
        st.markdown(
            f'<div class="card-title">{op.get("titulo","(sem título)")}</div>'
            f'<div class="card-meta">{op.get("local","")} &nbsp;·&nbsp; {op.get("horario","")}</div>'
            f'<div class="card-body">{op.get("descricao","")}</div>'
            + (f'<div class="card-meta" style="margin-top:6px;">'
               f'<a href="{link}" target="_blank">{link}</a></div>' if link else ''),
            unsafe_allow_html=True,
        )

        with st.expander("Editar / remover"):
            with st.form(f"edit_op_{op['id']}"):
                e_titulo = st.text_input("Título", value=op.get("titulo", ""))
                e_desc = st.text_area("Descrição", value=op.get("descricao", ""), height=110)
                ec1, ec2 = st.columns(2)
                e_local = ec1.text_input("Local", value=op.get("local", ""))
                e_horario = ec2.text_input("Horário", value=op.get("horario", ""))
                e_link = st.text_input("Link de inscrição (URL)", value=op.get("link_inscricao") or "", key=f"link_{op['id']}")
                oc1, oc2 = st.columns(2)
                save = oc1.form_submit_button("Salvar alterações")
                delete = oc2.form_submit_button("Remover")

            if save:
                payload = {
                    "titulo": e_titulo,
                    "descricao": e_desc,
                    "local": e_local,
                    "horario": e_horario,
                    "link_inscricao": e_link or None,
                }
                with st.spinner("Salvando alterações..."):
                    r = make_request("PUT", f"/oportunidades/{op['id']}", payload)
                if r is not None and r.status_code == 200:
                    flash("Oportunidade atualizada!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))
            if delete:
                with st.spinner("Removendo..."):
                    r = make_request("DELETE", f"/oportunidades/{op['id']}")
                if r is not None and r.status_code == 200:
                    flash("Oportunidade removida!")
                    st.rerun()
                elif r is not None:
                    st.error(error_detail(r))
