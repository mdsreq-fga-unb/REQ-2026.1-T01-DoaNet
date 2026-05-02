from datetime import date


def individual_feed_item_serializer(feed_item) -> dict:
    return {
        "id": str(feed_item["_id"]),
        "title": feed_item["title"],
        "type": feed_item["type"],
        "description": feed_item["description"]
        
    }

def list_feed_items_serializer(feed_items) -> list:
    return [individual_feed_item_serializer(feed_item) for feed_item in feed_items]