from typing import Annotated

from pydantic import UUID4, AfterValidator

ItemUID = Annotated[UUID4, AfterValidator(str)]
ItemDescription = Annotated[str, AfterValidator(str)]
ItemName = Annotated[str, AfterValidator(str)]
