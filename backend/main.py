from contextlib import asynccontextmanager

from fastapi import FastAPI

from . import models
from .database import engine
from .router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
