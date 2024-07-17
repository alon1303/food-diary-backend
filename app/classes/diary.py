from pydantic import BaseModel
from page import Page
from datetime import date
from datetype import Date
class Diary(BaseModel):
    name: str
    format: str
    userName:str
    pages:list[Page] = []
    create_date: Date = date
