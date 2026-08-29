from fastapi import APIRouter
from app.db.mongodb import database_status

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health():
    return {"status": "ok", "service": "neurox-prototype-api", "database": database_status()}
