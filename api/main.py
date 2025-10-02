from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from models import Base
from database import engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
