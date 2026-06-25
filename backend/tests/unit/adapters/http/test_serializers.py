from domain.entities.feed_item import FeedItem
from adapters.http.serializers import feed_item_to_dict, feed_items_to_list


def test_feed_item_to_dict():
    item = FeedItem(id="1", title="Cesta basica", type="sem_evento", description="Doacao")

    payload = feed_item_to_dict(item)

    assert payload["id"] == "1"
    assert payload["title"] == "Cesta basica"
    assert payload["type"] == "sem_evento"
    assert payload["description"] == "Doacao"
    assert payload["image_url"] is None
    assert payload["image_path"] is None
    assert payload["event_location"] is None
    assert payload["event_date"] is None
    assert payload["event_url"] is None
    assert "created_at" in payload


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

    assert len(payload) == 2

    assert payload[0]["id"] == "1"
    assert payload[0]["title"] == "Cesta basica"
    assert payload[0]["type"] == "sem_evento"
    assert payload[0]["description"] == "Doacao"

    assert payload[1]["id"] == "2"
    assert payload[1]["title"] == "Campanha do agasalho"
    assert payload[1]["type"] == "com_evento"
    assert payload[1]["description"] == "Evento atrelado"
