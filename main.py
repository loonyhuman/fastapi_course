from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import STaskAdd


from router import router as tasks_router

app = FastAPI()

# Контекстный менеджер для управления БД
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    
    await create_tables()
    print("База готова к работе")
    
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
