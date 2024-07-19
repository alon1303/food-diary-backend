from pydantic import BaseModel
from datetime import date

class Page(BaseModel):
    name:str
    content:str
    date:str

class Diary(BaseModel):
    name: str
    format: str
    userName:str
    pages:list[Page] = []
    create_date: date = date.today()

class User(BaseModel):
    user_name:str
    password:str

