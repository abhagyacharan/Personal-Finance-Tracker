# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import HTTPBearer
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.core.config import settings
import uvicorn

# Import routers (we'll create these next)
# from app.routers import auth, users, resumes, job_descriptions, mock_sessions, file_parser, user_metrics

app = FastAPI(
    title="PFT API",
    description="Personal Finance Tracker API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Security
# security = HTTPBearer()

# Include routers
# app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
# app.include_router(users.router, prefix="/api/users", tags=["Users"])
# app.include_router(resumes.router, prefix="/api/resumes", tags=["Resumes"])
# app.include_router(job_descriptions.router, prefix="/api/job-descriptions", tags=["Job Descriptions"])
# app.include_router(file_parser.router, prefix="/api/parse", tags=["File Parsing"])
# app.include_router(mock_sessions.router, prefix="/api/mock-sessions", tags=["Mock Sessions"])
# app.include_router(user_metrics.router, prefix="/api/user-metrics", tags=["User Metrics"])

@app.get("/")
async def root():
    return {"message": "PFT API is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)