import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER = os.getenv("MONGODB_CLUSTER")
MONGODB_APP_NAME = os.getenv("MONGODB_APP_NAME", "doa-net")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "doa_net_db")

if not all([MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER]):
	raise RuntimeError(
		"Missing MongoDB settings. Configure MONGODB_USERNAME, MONGODB_PASSWORD and MONGODB_CLUSTER in backend/.env"
	)

MONGODB_URI = (
	f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}"
	f"@{MONGODB_CLUSTER}/?appName={MONGODB_APP_NAME}"
)

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
collection_name = db["org_feed"]