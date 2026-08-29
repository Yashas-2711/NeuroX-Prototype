import os
from datetime import datetime, timezone
from pymongo import MongoClient
from pymongo.errors import PyMongoError

_client = None
_database = None

def _load_env_file():
    """Load local backend/.env without printing or committing its values."""
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
    if not os.path.exists(env_path):
        return
    with open(env_path, encoding='utf-8') as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

def get_database():
    global _client, _database
    _load_env_file()
    uri = os.getenv('MONGODB_URI', '').strip()
    if not uri: raise RuntimeError('MONGODB_URI is not configured')
    if _database is None:
        _client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        _client.admin.command('ping')
        _database = _client[os.getenv('MONGODB_DATABASE', 'neurox_prototype')]
    return _database

def database_status():
    try: get_database(); return 'connected'
    except Exception: return 'unavailable'

def create_challenge(document):
    db = get_database(); document = {**document, 'created_at': datetime.now(timezone.utc).isoformat()}
    result = db.challenges.insert_one(document); return str(result.inserted_id)

def get_challenge(identifier):
    from bson import ObjectId
    db = get_database(); document = db.challenges.find_one({'_id': ObjectId(identifier)})
    if not document: return None
    document['id'] = str(document.pop('_id')); return document

def create_solution(document):
    db = get_database(); document = {**document, 'created_at': datetime.now(timezone.utc).isoformat()}
    result = db.solutions.insert_one(document); return str(result.inserted_id)

def get_solution(identifier):
    from bson import ObjectId
    db = get_database(); document = db.solutions.find_one({'_id': ObjectId(identifier)})
    if not document: return None
    document['id'] = str(document.pop('_id')); return document
