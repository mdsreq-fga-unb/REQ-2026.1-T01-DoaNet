import pytest
from pydantic import ValidationError

from domain.entities.feed_item import FeedItem


def test_feed_item_accepts_required_fields():
    item = FeedItem(title="Cesta basica", type="sem_evento", description="Doacao")

    assert item.id is None
    assert item.title == "Cesta basica"
    assert item.type == "sem_evento"
    assert item.description == "Doacao"


def test_feed_item_requires_title():
    with pytest.raises(ValidationError):
        FeedItem(type="sem_evento", description="Doacao")


def test_feed_item_requires_type():
    with pytest.raises(ValidationError):
        FeedItem(title="Cesta basica", description="Doacao")


def test_feed_item_requires_description():
    with pytest.raises(ValidationError):
        FeedItem(title="Cesta basica", type="sem_evento")
