from application.services.feed_service import FeedService
from domain.entities.feed_item import FeedItem


class FakeFeedRepository:
    def __init__(self) -> None:
        self.items = []
        self.last_added = None
        self.last_updated = None
        self.last_deleted = None

    def list_all(self):
        return list(self.items)

    def add(self, item: FeedItem) -> None:
        self.last_added = item
        self.items.append(item)

    def update_item(self, item_id: str, item: FeedItem) -> bool:
        self.last_updated = (item_id, item)
        return True

    def delete(self, item_id: str) -> bool:
        self.last_deleted = item_id
        return True


def test_list_items_returns_repo_items():
    repo = FakeFeedRepository()
    repo.items = [
        FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao"),
        FeedItem(
            id="2",
            title="Campanha do agasalho",
            type="com_evento",
            description="Evento atrelado",
        ),
    ]

    service = FeedService(repo)
    result = service.list_items()

    assert result == repo.items


def test_add_item_delegates_to_repo():
    repo = FakeFeedRepository()
    service = FeedService(repo)

    item = FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao")
    service.add_item(item)

    assert repo.last_added == item
    assert repo.items == [item]


def test_update_item_delegates_to_repo():
    repo = FakeFeedRepository()
    service = FeedService(repo)

    item = FeedItem(
        id="1",
        title="Cesta basica atualizada",
        type="com_evento",
        description="Atualizado",
    )
    result = service.update_item("1", item)

    assert result is True
    assert repo.last_updated == ("1", item)


def test_delete_item_delegates_to_repo():
    repo = FakeFeedRepository()
    service = FeedService(repo)

    result = service.delete_item("1")

    assert result is True
    assert repo.last_deleted == "1"
