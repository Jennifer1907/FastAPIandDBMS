# main.py content placeholder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Create FastAPI app
app = FastAPI(
    title="EMR System API",
    description="Electronic Medical Record System API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic health check endpoint
@app.get("/ping")
def ping():
    return {"message": "pong"}

# Import and include routers
from app.routers import medical, patients, visits

app.include_router(patients.router, prefix="/api/v1", tags=["patients"])
app.include_router(visits.router, prefix="/api/v1", tags=["visits"])
app.include_router(medical.router, prefix="/api/v1", tags=["medical"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)