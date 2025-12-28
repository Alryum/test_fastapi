from src.item.infrastructure.db.interface import ItemRepositoryInterface
from src.item.infrastructure.db.repo import ItemRepository
from src.shared.application.commands.abs_uow import AbstractUOW, SQLAlchemyAbstractUOW


class ItemAbstractUOW(AbstractUOW):
    repo_interface: ItemRepositoryInterface


class ItemUOW(ItemAbstractUOW, SQLAlchemyAbstractUOW):
    async def __aenter__(self):
        self._session = self._session_factory()
        self.repo_interface = ItemRepository(self._session)
