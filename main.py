from fastapi import FastAPI
from router import router as task_router

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(
    lifespan=lifespan
)
app.include_router(task_router)
