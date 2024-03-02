from typing import List

from pydantic import BaseModel


class Vector(BaseModel):
    vector: List[int]
    vector_size: int
    vector_name: str
    vector_type: str
    vector_description: str
