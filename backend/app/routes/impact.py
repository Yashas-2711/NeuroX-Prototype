import logging
from fastapi import APIRouter, HTTPException
from app.schemas.challenge import ImpactRequest
from app.services.impact import assess_impact

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/challenges", tags=["impact"])

@router.post("/impact")
def impact_assessment(challenge: ImpactRequest):
    try: return {"status": "success", "impact": assess_impact(challenge.model_dump())}
    except Exception:
        logger.exception("Impact assessment failed")
        raise HTTPException(status_code=503, detail="Impact analysis is temporarily unavailable.")
