import logging
from fastapi import APIRouter, HTTPException
from app.schemas.challenge import SimilarityRequest
from app.services.similarity import find_similar

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/challenges", tags=["similarity"])

@router.post("/similar")
def similar_challenges(challenge: SimilarityRequest):
    try: return {"status": "success", "results": find_similar(challenge.model_dump())}
    except Exception:
        logger.exception("Similarity analysis failed")
        raise HTTPException(status_code=503, detail="Similarity analysis is temporarily unavailable.")
