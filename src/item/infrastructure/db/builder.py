from src.item import aggregators
from src.shared import db_models


def build_ORM(item: aggregators.Item) -> db_models.Item:
    return db_models.Item(uuid=item.uid, name=item.name, description=item.description)


def build_agg(item_orm: db_models.Item) -> aggregators.Item:
    return aggregators.Item(
        uid=item_orm.uuid, name=item_orm.name, description=item_orm.description
    )
