from typing import List

from domain.entities.feed_item import FeedItem


def feed_item_to_dict(item: FeedItem) -> dict:
    if hasattr(item, "model_dump"):
        data = item.model_dump()
    else:
        data = item.dict()
    return {
        "id": data.get("id"),
        "title": data["title"],
        "type": data["type"],
        "description": data["description"],
        "image_url": data["image_url"],
        "image_path": data["image_path"],
        "event_location": data["event_location"],
        "event_date": data["event_date"],
        "event_url": data["event_url"],
        "created_at": data["created_at"].isoformat() if data.get("created_at") else None
    }


def feed_items_to_list(items: List[FeedItem]) -> list:
    return [feed_item_to_dict(item) for item in items]

from domain.entities.oportunidade import OportunidadeVoluntariado

def oportunidade_to_dict(item: OportunidadeVoluntariado) -> dict:
    if hasattr(item, "model_dump"):
        data = item.model_dump()
    else:
        data = item.dict()
    return {
        "id": data.get("id"),
        "titulo": data.get("titulo"),
        "descricao": data.get("descricao"),
        "local": data.get("local"),
        "horario": data.get("horario"),
        "vagas_totais": data.get("vagas_totais"),
        "vagas_preenchidas": data.get("vagas_preenchidas"),
        "imagem_url": data.get("imagem_url"),
        "ativo": data.get("ativo"),
    }

def oportunidades_to_list(items: List[OportunidadeVoluntariado]) -> list:
    return [oportunidade_to_dict(item) for item in items]


from domain.entities.transparencia_record import TransparenciaRecord


def transparencia_record_to_dict(record: TransparenciaRecord) -> dict:
    if hasattr(record, "model_dump"):
        data = record.model_dump()
    else:
        data = record.dict()
    return {
        "id": data.get("id"),
        "tipo": data.get("tipo"),
        "valor": data.get("valor"),
        "data": data["data"].isoformat() if data.get("data") else None,
        "descricao": data.get("descricao"),
        "created_at": data["created_at"].isoformat() if data.get("created_at") else None,
        "created_by": data.get("created_by"),
    }


def transparencia_records_to_list(records: List[TransparenciaRecord]) -> list:
    return [transparencia_record_to_dict(r) for r in records]