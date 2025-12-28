from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from src.item.endpoints.endpoints import zalupa_router

main_router = APIRouter()
main_router.include_router(zalupa_router)
app = FastAPI()
app.include_router(main_router)
