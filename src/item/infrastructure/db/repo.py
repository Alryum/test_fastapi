from .interface import ItemRepositoryInterface
from sqlalchemy import select
from src.item.aggregators.item import Item
from src.shared import db_models
from src.shared.app_types.item_types import ItemName
from src.shared.infrastructure.db.repo import SQLAlchemyRepo
from .builder import build_ORM, build_agg


class ItemRepository(ItemRepositoryInterface, SQLAlchemyRepo):
    async def create(self, item: Item):
        item_orm = build_ORM(item)
        self.__session.add(item_orm)

    async def get_by_name(self, name: ItemName) -> Item:
        statement = select(
            db_models.Item,
        ).where(db_models.Item.name == name)
        item_orm = await self.__session.scalar(statement)
        return build_agg(item_orm)
