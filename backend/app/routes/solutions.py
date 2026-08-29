import logging
from fastapi import APIRouter, HTTPException
from app.schemas.challenge import SimilarityRequest
from app.services.solutions import recommend_solutions
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/challenges", tags=["solutions"])
@router.post("/solutions")
def solution_recommendations(challenge: SimilarityRequest):
    try: return {"status": "success", "recommendations": recommend_solutions(challenge.model_dump())}
    except Exception:
        logger.exception("Solution recommendation failed")
        raise HTTPException(status_code=503, detail="Solution recommendations are temporarily unavailable.")
