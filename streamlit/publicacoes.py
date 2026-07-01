"""Publicações (org_feed) — posts e eventos do feed."""
import streamlit as st

from config import FEED_TYPES, FEED_TYPE_META
from api import make_request, make_multipart_request, error_detail, feed_result_ok
from ui import flash, show_flash


def publicacoes_section():
    st.subheader("Publicações")
    st.caption("Posts e eventos do feed. A imagem é enviada por upload (vai para o GCS).")
    show_flash()

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
            # Upload de imagem apenas para posts comuns (eventos não têm imagem).
            if ptype == "evento":
                image = None
                st.markdown("**Dados do evento** (obrigatórios):")
                ec1, ec2 = st.columns(2)
                event_location = ec1.text_input("Local do evento")
                event_date = ec2.text_input("Data do evento", placeholder="ex: 2026-06-20")
                event_url = st.text_input("Link do evento (URL)")
            else:
                image = st.file_uploader("Imagem (opcional)", type=["png", "jpg", "jpeg", "webp"])
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
                    with st.spinner("Publicando..."):
                        resp = make_multipart_request("POST", "/feed", data=data, files=files)
                    ok, msg = feed_result_ok(resp)
                    if ok:
                        flash("Publicação criada com sucesso!")
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
                # Upload de imagem apenas para posts comuns (eventos não têm imagem).
                if new_type == "evento":
                    new_image = None
                    st.caption("Dados do evento (obrigatórios):")
                    ec1, ec2 = st.columns(2)
                    new_loc = ec1.text_input("Local", value=item.get("event_location") or "", key=f"loc_{item['id']}")
                    new_date = ec2.text_input("Data", value=item.get("event_date") or "", key=f"date_{item['id']}")
                    new_url = st.text_input("Link (URL)", value=item.get("event_url") or "", key=f"url_{item['id']}")
                else:
                    new_image = st.file_uploader(
                        "Trocar imagem (opcional — mantém a atual se vazio)",
                        type=["png", "jpg", "jpeg", "webp"], key=f"img_{item['id']}",
                    )
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
                    with st.spinner("Salvando alterações..."):
                        r = make_multipart_request("PUT", f"/feed/{item['id']}", data=data, files=files)
                    ok, msg = feed_result_ok(r)
                    if ok:
                        flash("Publicação atualizada!")
                        st.rerun()
                    elif r is not None:
                        st.error(msg)
            if delete:
                with st.spinner("Removendo..."):
                    r = make_request("DELETE", f"/feed/{item['id']}")
                ok, msg = feed_result_ok(r)
                if ok:
                    flash("Publicação removida!")
                    st.rerun()
                elif r is not None:
                    st.error(msg)
