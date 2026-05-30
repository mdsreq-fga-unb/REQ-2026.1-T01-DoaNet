import os
from pathlib import Path

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient


BASE_DIR = Path(__file__).resolve().parents[3]
load_dotenv(BASE_DIR / ".env")

_client = None
_collection = None


def _get_settings():
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")
    cluster = os.getenv("MONGODB_CLUSTER")
    app_name = os.getenv("MONGODB_APP_NAME", "doa-net")
    db_name = os.getenv("MONGODB_DB_NAME", "doa_net_db")

    if not all([username, password, cluster]):
        raise RuntimeError(
            "Missing MongoDB settings. Configure MONGODB_USERNAME, MONGODB_PASSWORD and MONGODB_CLUSTER in backend/.env"
        )

    uri = f"mongodb+srv://{username}:{password}@{cluster}/?appName={app_name}"
    return uri, db_name


def get_collection():
    global _client
    global _collection

    if _collection is None:
        uri, db_name = _get_settings()
        _client = MongoClient(uri, tlsCAFile=certifi.where())
        db = _client[db_name]
        _collection = db["org_feed"]

    return _collection

_oportunidade_collection = None

def get_oportunidade_collection():
    global _client
    global _oportunidade_collection

    if _oportunidade_collection is None:
        uri, db_name = _get_settings()
        if _client is None:
            _client = MongoClient(uri, tlsCAFile=certifi.where())
        db = _client[db_name]
        _oportunidade_collection = db["oportunidades"] # Nova coleção no banco!

    return _oportunidade_collection