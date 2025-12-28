from src.item.aggregators.item import Item
from src.item.application.commands.uow import ItemAbstractUOW
from src.shared.app_types.item_types import ItemDescription, ItemName


class CreateItemCommand:
    def __init__(
        self,
        unit_of_work: ItemAbstractUOW,
    ):
        self._uow = unit_of_work

    async def handle(
        self,
        name: ItemName,
        description: ItemDescription,
    ):
        async with self._uow as uow:
            if await uow.repo_interface.get_by_name(name=name):
                raise Exception("ZALUPA")
            aggregate_item = Item(name=name, description=description)
            await uow.repo_interface.create(aggregate_item)
            await uow.repo_interface.commit()
