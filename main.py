from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1 import  api_v1_router
from src.api.v1.super_admin import create_super_admin
from src.base.pg_db import get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_gen = get_db()
    db: AsyncSession = await anext(db_gen)

    try:
        await create_super_admin(db)
        yield
    finally:
        await db.close()

app = FastAPI(lifespan=lifespan)

app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
