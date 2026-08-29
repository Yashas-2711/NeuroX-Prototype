from fastapi import APIRouter
from app.schemas.challenge import ChallengeSubmission, ChallengeAcknowledgement
from app.services.classifier import classify_challenge

router = APIRouter(prefix="/api/challenges", tags=["challenges"])


@router.post("/analyze", response_model=ChallengeAcknowledgement)
def analyze_challenge(challenge: ChallengeSubmission):
    analysis = classify_challenge(f"{challenge.title}. {challenge.description}. Domain: {challenge.domain}")
    return {"status": "success", "message": "Challenge received successfully", "challenge": challenge, "ai_analysis": analysis}
