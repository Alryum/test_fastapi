from src.item.application.commands.create import CreateItemCommand
from src.item.application.commands.uow import ItemUOW
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from src.config import db_settings


async_session_factory: async_sessionmaker = async_sessionmaker(
    create_async_engine(db_settings.db_url),
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


def build_create_command_handler():
    return CreateItemCommand(ItemUOW(async_session_factory))
