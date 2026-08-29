from pydantic import BaseModel


class ChallengeSubmission(BaseModel):
    title: str
    description: str
    domain: str
    location: str
    affectedPeople: str = ""


class ChallengeAcknowledgement(BaseModel):
    status: str
    message: str
    challenge: ChallengeSubmission
    ai_analysis: dict | None = None
