from pydantic import BaseModel, Field

class PersistedChallenge(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    domain: str = Field(min_length=1)
    location: str = Field(min_length=1)
    affected_people: str = ""

class PersistedSolution(BaseModel):
    challenge_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    implementation_approach: str = Field(min_length=1)
    technologies: list[str] = []
    expected_beneficiaries: str = ""
