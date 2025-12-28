from src.item.application.commands.uow import ItemAbstractUOW
from src.shared.app_types.item_types import ItemDescription, ItemName
from src.item.aggregators.item import Item


class CreateItemCommand:
    def __init__(self, uow: ItemAbstractUOW):
        self._uow = uow

    async def handle(self, name: ItemName, description: ItemDescription):
        async with self._uow as uow:
            if item := await uow.repo_interface.get_by_name(name=name):
                raise Exception("ZALUPA")
            aggregate_item = Item(name=name, description=description)
            await uow.repo_interface.create(aggregate_item)
            await uow.commit()
