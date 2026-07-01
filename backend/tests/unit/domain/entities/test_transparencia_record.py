import pytest
from pydantic import ValidationError

from domain.entities.transparencia_record import TransparenciaRecord, TipoRegistro


def test_transparencia_record_accepts_required_fields():
    record = TransparenciaRecord(
        tipo=TipoRegistro.DOACAO_EXTERNA,
        valor=100.0,
        data="2025-06-01T00:00:00",
        descricao="Doação via Pix",
    )

    assert record.id is None
    assert record.tipo == TipoRegistro.DOACAO_EXTERNA
    assert record.valor == 100.0
    assert record.descricao == "Doação via Pix"
    assert record.created_at is not None
    assert record.created_by is None


def test_transparencia_record_accepts_despesa():
    record = TransparenciaRecord(
        tipo=TipoRegistro.DESPESA,
        valor=50.0,
        data="2025-06-15T00:00:00",
        descricao="Material de escritório",
    )

    assert record.tipo == TipoRegistro.DESPESA
    assert record.valor == 50.0
    assert record.descricao == "Material de escritório"


def test_transparencia_record_rejects_zero_valor():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            tipo=TipoRegistro.DOACAO_EXTERNA,
            valor=0,
            data="2025-06-01T00:00:00",
            descricao="Teste",
        )


def test_transparencia_record_rejects_negative_valor():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            tipo=TipoRegistro.DOACAO_EXTERNA,
            valor=-10.0,
            data="2025-06-01T00:00:00",
            descricao="Teste",
        )


def test_transparencia_record_rejects_invalid_tipo():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            tipo="invalido",
            valor=100.0,
            data="2025-06-01T00:00:00",
            descricao="Teste",
        )


def test_transparencia_record_requires_tipo():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            valor=100.0,
            data="2025-06-01T00:00:00",
            descricao="Teste",
        )


def test_transparencia_record_requires_valor():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            tipo=TipoRegistro.DOACAO_EXTERNA,
            data="2025-06-01T00:00:00",
            descricao="Teste",
        )


def test_transparencia_record_requires_descricao():
    with pytest.raises(ValidationError):
        TransparenciaRecord(
            tipo=TipoRegistro.DOACAO_EXTERNA,
            valor=100.0,
            data="2025-06-01T00:00:00",
        )


def test_transparencia_record_created_at_auto_generated():
    record = TransparenciaRecord(
        tipo=TipoRegistro.DOACAO_EXTERNA,
        valor=100.0,
        data="2025-06-01T00:00:00",
        descricao="Teste",
    )
    assert record.created_at is not None


def test_transparencia_record_with_created_by():
    record = TransparenciaRecord(
        tipo=TipoRegistro.DESPESA,
        valor=200.0,
        data="2025-06-01T00:00:00",
        descricao="Aluguel",
        created_by="admin@doanet.org",
    )
    assert record.created_by == "admin@doanet.org"
