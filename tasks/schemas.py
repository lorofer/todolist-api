from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class Task(BaseModel):
    id: int
    title: Annotated[str, MaxLen(25)]
    description: str