from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router
from app.routes.challenges import router as challenge_router

app = FastAPI(title="NeuroX Prototype API")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])


@app.get("/")
def root():
    return {
        "message": "NeuroX Prototype API is running"
    }


app.include_router(health_router)
app.include_router(challenge_router)
