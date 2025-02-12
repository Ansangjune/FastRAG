from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import v1

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(v1.completions.router, prefix="/v1/chat/completions")