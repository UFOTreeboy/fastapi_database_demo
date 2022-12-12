from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
    id:int
    name: str
    task: float
