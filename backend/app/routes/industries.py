import logging
from fastapi import APIRouter, HTTPException
from app.schemas.challenge import SimilarityRequest
from app.services.industry_matching import match_industries
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/challenges", tags=["industries"])
@router.post("/industries")
def industry_matches(challenge: SimilarityRequest):
    try: return {"status":"success","matches":match_industries(challenge.model_dump())}
    except Exception:
        logger.exception("Industry matching failed")
        raise HTTPException(status_code=503, detail="Industry matching is temporarily unavailable.")
