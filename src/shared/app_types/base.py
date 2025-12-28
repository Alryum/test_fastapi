from typing import Annotated
from pydantic import UUID4, AfterValidator
from datetime import datetime
from fastapi import Header

DateTime = Annotated[datetime, ...]
EtagType = Annotated[int, Header()]
ETagValue = Annotated[int, ...]

UserUID = Annotated[UUID4, AfterValidator(str)]
