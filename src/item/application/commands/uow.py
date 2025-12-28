from src.item.infrastructure.db.interface import ItemRepositoryInterface
from src.item.infrastructure.db.repo import ItemRepository
from src.shared.application.commands.abs_uow import AbstractUOW, SQLAlchemyAbstractUOW
from typing import Any

class ItemAbstractUOW(AbstractUOW):
    repo_interface: ItemRepositoryInterface


class ItemUOW(ItemAbstractUOW, SQLAlchemyAbstractUOW):
    
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Инициализация единицы работы обработчика для правил коллекций.

        Args:
            access_controller_builder: Функция для постройки контроллера пользовательских возможностей.
            *args: Позиционные аргументы
            **kwargs: Именованные аргументы
        """
        super().__init__(*args, **kwargs)
        
    async def __aenter__(self,):
        self._session = self._session_factory()
        self.repo_interface = ItemRepository(self._session)
        return self