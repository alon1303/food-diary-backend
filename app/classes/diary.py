from pydantic import BaseModel
from .page import Page
from typing import List
class Diary(BaseModel):
    name: str
    format: str
    pages: List[Page]
    date: str
