"""FastAPI 入口

启动:uvicorn app.main:app --reload
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import agent, chat, documents
from app.core.config import get_settings
from app.core.logging import setup_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    setup_logging()
    yield


settings = get_settings()

app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(agent.router, prefix="/api/v1/agent", tags=["Agent"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["RAG"])


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
