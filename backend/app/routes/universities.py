import logging
from fastapi import APIRouter, HTTPException
from app.schemas.challenge import SimilarityRequest
from app.services.university_matching import match_universities
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/challenges", tags=["universities"])
@router.post("/universities")
def university_matches(challenge: SimilarityRequest):
    try: return {"status": "success", "matches": match_universities(challenge.model_dump())}
    except Exception:
        logger.exception("University matching failed")
        raise HTTPException(status_code=503, detail="University matching is temporarily unavailable.")
