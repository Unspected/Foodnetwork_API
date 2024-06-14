from typing import Dict
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    thumb: str


class Categories(BaseModel):
    categories: Dict[str, Category]