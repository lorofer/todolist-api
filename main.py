from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import AsyncIterator

from database import base_ormar_config
from config import settings
from tasks.api import task_router
from tasks.models import Task


def get_lifespan(config):
    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        if not config.database.is_connected:
            await config.database.connect()

        yield

        if config.database.is_connected:
            await config.database.disconnect()
    return lifespan


base_ormar_config.metadata.create_all(base_ormar_config.engine)
app = FastAPI(lifespan=get_lifespan(base_ormar_config))

origins = [settings.CLIENT_ORIGIN]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(task_router, prefix="/api/tasks")
