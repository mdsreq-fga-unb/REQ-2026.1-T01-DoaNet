import pytest
from domain.entities.organization import Organization
from application.services.organization_service import OrganizationService


class FakeOrganizationRepository:
    def __init__(self):
        self.items = []

    def find_by_org_id(self, org_id: str):
        for item in self.items:
            if item.org_id == org_id:
                return item
        return None

    def create(self, org: Organization) -> Organization:
        self.items.append(org)
        return org

    def update(self, org_id: str, org: Organization) -> bool:
        for idx, item in enumerate(self.items):
            if item.org_id == org_id:
                self.items[idx] = org
                return True
        return False


def _make_org(**kwargs) -> Organization:
    defaults = {
        "org_id": "test-org",
        "name": "Org Teste",
        "description": "Descrição teste",
        "primary_color": "#FF0000",
        "background_color": "#FFFFFF",
        "logo_url": None,
    }
    defaults.update(kwargs)
    return Organization(**defaults)


# ----------------------------------------------------------------------------
# get_config
# ----------------------------------------------------------------------------
def test_get_config_returns_org_when_found():
    repo = FakeOrganizationRepository()
    repo.items.append(_make_org())
    service = OrganizationService(repo)

    result = service.get_config("test-org")

    assert result is not None
    assert result.org_id == "test-org"
    assert result.name == "Org Teste"


def test_get_config_returns_none_when_not_found():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    result = service.get_config("nao-existe")

    assert result is None


# ----------------------------------------------------------------------------
# create_or_update — criação
# ----------------------------------------------------------------------------
def test_create_or_update_creates_when_not_exists():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    org = _make_org()
    result = service.create_or_update(org)

    assert len(repo.items) == 1
    assert result.org_id == "test-org"


def test_create_or_update_persists_all_fields():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    org = _make_org(
        name="MoveEduca",
        description="Educação para todos",
        primary_color="#0088FF",
        background_color="#FAFAFA",
        logo_url="https://cdn.example.com/logo.png",
    )
    service.create_or_update(org)

    saved = repo.items[0]
    assert saved.name == "MoveEduca"
    assert saved.description == "Educação para todos"
    assert saved.primary_color == "#0088FF"
    assert saved.background_color == "#FAFAFA"
    assert saved.logo_url == "https://cdn.example.com/logo.png"


# ----------------------------------------------------------------------------
# create_or_update — atualização
# ----------------------------------------------------------------------------
def test_create_or_update_updates_when_exists():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    service.create_or_update(_make_org(name="Nome Antigo"))
    service.create_or_update(_make_org(name="Nome Novo"))

    assert len(repo.items) == 1
    assert repo.items[0].name == "Nome Novo"


def test_create_or_update_updates_primary_color():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    service.create_or_update(_make_org(primary_color="#FF0000"))
    service.create_or_update(_make_org(primary_color="#00FF00"))

    assert repo.items[0].primary_color == "#00FF00"


def test_create_or_update_preserves_logo_url_on_update():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    service.create_or_update(_make_org(logo_url="https://cdn.example.com/logo.png"))
    service.create_or_update(_make_org(logo_url="https://cdn.example.com/logo.png", name="Nome Novo"))

    assert repo.items[0].logo_url == "https://cdn.example.com/logo.png"


def test_create_or_update_different_orgs_dont_interfere():
    repo = FakeOrganizationRepository()
    service = OrganizationService(repo)

    service.create_or_update(_make_org(org_id="org-a", name="Org A"))
    service.create_or_update(_make_org(org_id="org-b", name="Org B"))

    assert len(repo.items) == 2
    assert service.get_config("org-a").name == "Org A"
    assert service.get_config("org-b").name == "Org B"