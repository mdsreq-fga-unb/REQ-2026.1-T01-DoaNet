from domain.entities.feed_item import FeedItem
from adapters.http.serializers import feed_item_to_dict, feed_items_to_list


def test_feed_item_to_dict():
    item = FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao")

    payload = feed_item_to_dict(item)

    assert payload == {
        "id": "1",
        "title": "Cesta basica",
        "type": "sem_evento",
        "description": "Doacao",
    }


def test_feed_items_to_list():
    items = [
        FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao"),
        FeedItem(
            id="2",
            title="Campanha do agasalho",
            type="com_evento",
            description="Evento atrelado",
        ),
    ]

    payload = feed_items_to_list(items)

    assert payload == [
        {
            "id": "1",
            "title": "Cesta basica",
            "type": "sem_evento",
            "description": "Doacao",
        },
        {
            "id": "2",
            "title": "Campanha do agasalho",
            "type": "com_evento",
            "description": "Evento atrelado",
        },
    ]
