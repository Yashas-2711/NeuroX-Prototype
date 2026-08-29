"""Reusable MiniLM similarity service for the local demo challenge set."""
import logging
from threading import Lock
from app.data.demo_challenges import DEMO_CHALLENGES

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EXPECTED_EMBEDDING_DIMENSION = 384
logger = logging.getLogger(__name__)
_model = None
_demo_embeddings = None
_load_lock = Lock()

def _text(item): return f"{item['title']} {item['description']} {item['domain']}"
def _classification(score):
    if score >= 0.88: return "Potential Duplicate"
    if score >= 0.75: return "Related Challenge"
    return "Low Similarity"

def _load():
    """Load MiniLM and static demo embeddings once per backend process."""
    from sentence_transformers import SentenceTransformer
    global _model, _demo_embeddings
    if _model is not None: return _model, _demo_embeddings
    with _load_lock:
        if _model is None:
            model = SentenceTransformer(MODEL_NAME)
            dimension = model.get_embedding_dimension()
            if dimension != EXPECTED_EMBEDDING_DIMENSION:
                raise RuntimeError(f"MiniLM embedding dimension was {dimension}, expected {EXPECTED_EMBEDDING_DIMENSION}.")
            embeddings = model.encode([_text(item) for item in DEMO_CHALLENGES], convert_to_tensor=True, normalize_embeddings=True)
            _model, _demo_embeddings = model, embeddings
            logger.info("Loaded %s: %d-dimensional embeddings for %d demo challenges.", MODEL_NAME, dimension, len(DEMO_CHALLENGES))
    return _model, _demo_embeddings

def find_similar(challenge):
    from sentence_transformers import util
    model, embeddings = _load()
    query = model.encode(_text(challenge), convert_to_tensor=True, normalize_embeddings=True)
    scores = util.cos_sim(query, embeddings)[0]
    ranked = sorted(zip(DEMO_CHALLENGES, scores.tolist()), key=lambda pair: pair[1], reverse=True)[:3]
    return [{**item, "similarity": round(float(score), 4), "classification": _classification(float(score))} for item, score in ranked]
