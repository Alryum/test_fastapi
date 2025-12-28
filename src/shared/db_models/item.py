from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String
from src.shared.app_types import item_types
from src.shared.db_models.base import Base


class Item(Base):
    __tablename__ = "items"
    uuid: Mapped[item_types.ItemUID] = mapped_column(
        UUID, primary_key=True, doc="ZALUPA"
    )
    name: Mapped[item_types.ItemName] = mapped_column(String, doc="Name")
    description: Mapped[item_types.ItemDescription | None] = mapped_column(
        String, doc="Name", nullable=True
    )
