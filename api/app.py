from fastapi import FastAPI

app = FastAPI(title="DevOS Acceptance API")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "api"
    }

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "api",
        "message": "DevOS Multi-Service Acceptance API"
    }
