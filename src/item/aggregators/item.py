from typing import Self
from src.shared.app_types import item_types
from pydantic import Field, BaseModel
from uuid import uuid4


class Item(BaseModel):
    uid: item_types.ItemUID = Field(
        description="Уникальный ID предмета",
    )
    name: item_types.ItemName = Field(
        description="Название предмета",
    )
    description: item_types.ItemDescription | None = Field(
        description="Описание предмета",
    )

    @classmethod
    def create(cls, name, description) -> Self:
        return cls(uid=uuid4(), name=name, description=description)
