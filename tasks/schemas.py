from pydantic import BaseModel, Field
from typing import Annotated


class Task(BaseModel):
    id: int
    title: Annotated[str, Field(max_length=100)]
    description: Annotated[str, Field(max_length=1000)]


class AddTask(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    description: Annotated[str, Field(max_length=1000)]
