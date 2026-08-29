import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router
from app.routes.challenges import router as challenge_router
from app.routes.similarity import router as similarity_router
from app.routes.impact import router as impact_router
from app.routes.solutions import router as solutions_router
from app.routes.universities import router as universities_router
from app.routes.industries import router as industries_router
from app.routes.persistence import router as persistence_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

app = FastAPI(title="NeuroX Prototype API")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])


@app.get("/")
def root():
    return {
        "message": "NeuroX Prototype API is running"
    }


app.include_router(health_router)
app.include_router(challenge_router)
app.include_router(similarity_router)
app.include_router(impact_router)
app.include_router(solutions_router)
app.include_router(universities_router)
app.include_router(industries_router)
app.include_router(persistence_router)
