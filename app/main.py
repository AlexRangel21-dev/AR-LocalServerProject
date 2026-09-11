from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from database.database import Base, engine
import models  
from routers.health import router as health_router
from routers.auth import router as auth_router

app = FastAPI(
    title="Tools API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)