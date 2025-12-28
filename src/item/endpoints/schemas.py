from pydantic import BaseModel, Field
from src.shared.app_types import item_types


class CreateItemSchema(BaseModel):
    name: item_types.ItemName = Field(
        title="Название",
        description="desc",
        examples=[
            "zalupa",
        ],
    )
    description: item_types.ItemDescription | None = Field(
        title="Описание",
        description="desc",
        examples=[
            "desc",
        ],
    )
