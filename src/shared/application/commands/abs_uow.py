from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class AbstractUOW(ABC):
    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, ex_type, ex_instance, ex_traceback):
        pass

    @abstractmethod
    async def rollback(self):
        pass

    @abstractmethod
    async def commit(self):
        pass


class SQLAlchemyAbstractUOW(AbstractUOW):
    _session: AsyncSession

    def __init__(self, session_factory: async_sessionmaker):
        self._session_factory = session_factory

    async def __aexit__(self, ex_type, ex_instance, ex_traceback):
        await super().__aexit__(ex_type, ex_instance, ex_traceback)
        await self._session.close()

    async def rollback(self):
        await self._session.rollback()

    async def commit(self):
        await self._session.commit()
