from abc import ABC, abstractmethod
from src.item.aggregators.item import Item
from src.shared.app_types.item_types import ItemName
from src.shared import db_models


class ItemRepositoryInterface(ABC):
    @abstractmethod
    async def create(self, item: Item) -> None:
        pass

    @abstractmethod
    async def get_by_name(self, name: ItemName) -> db_models.Item:
        pass
