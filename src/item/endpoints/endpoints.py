from fastapi import APIRouter
from src.item.endpoints import deps, schemas

zalupa_router = APIRouter()


@zalupa_router.post("/items")
async def create_item(item_in: schemas.CreateItemSchema):
    command_handler = deps.build_create_command_handler()
    await command_handler.handle(item_in.name, item_in.description)
