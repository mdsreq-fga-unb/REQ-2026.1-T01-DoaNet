from datetime import datetime

from application.services.transparencia_service import TransparenciaService
from domain.entities.transparencia_record import TransparenciaRecord, TipoRegistro


class FakeTransparenciaRepository:
    def __init__(self) -> None:
        self.items = []
        self.last_added = None

    def list_all(self):
        return list(self.items)

    def add(self, record: TransparenciaRecord) -> None:
        self.last_added = record
        self.items.append(record)


def test_list_records_returns_repo_items():
    repo = FakeTransparenciaRepository()
    repo.items = [
        TransparenciaRecord(
            id="1",
            tipo=TipoRegistro.DOACAO,
            valor=100.0,
            data=datetime(2025, 6, 15),
            descricao="Doação via Pix",
        ),
        TransparenciaRecord(
            id="2",
            tipo=TipoRegistro.DESPESA,
            valor=50.0,
            data=datetime(2025, 6, 10),
            descricao="Material de escritório",
        ),
    ]

    service = TransparenciaService(repo)
    result = service.list_records()

    assert result == repo.items
    assert len(result) == 2


def test_list_records_returns_empty_when_no_items():
    repo = FakeTransparenciaRepository()
    service = TransparenciaService(repo)

    result = service.list_records()

    assert result == []


def test_add_record_delegates_to_repo():
    repo = FakeTransparenciaRepository()
    service = TransparenciaService(repo)

    record = TransparenciaRecord(
        tipo=TipoRegistro.DOACAO,
        valor=250.0,
        data=datetime(2025, 6, 20),
        descricao="Doação em dinheiro",
        created_by="admin@doanet.org",
    )
    service.add_record(record)

    assert repo.last_added == record
    assert repo.items == [record]


def test_add_record_despesa_delegates_to_repo():
    repo = FakeTransparenciaRepository()
    service = TransparenciaService(repo)

    record = TransparenciaRecord(
        tipo=TipoRegistro.DESPESA,
        valor=300.0,
        data=datetime(2025, 6, 25),
        descricao="Aluguel do espaço",
        created_by="admin@doanet.org",
    )
    service.add_record(record)

    assert repo.last_added == record
    assert repo.last_added.tipo == TipoRegistro.DESPESA
