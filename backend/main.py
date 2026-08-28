from fastapi import FastAPI

app = FastAPI(title="NeuroX Prototype API")


@app.get("/")
def root():
    return {
        "message": "NeuroX Prototype API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }