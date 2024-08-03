from pydantic import BaseModel
from datetime import datetime

class Page(BaseModel):
    name:str
    content:str
    date:str

class Diary(BaseModel):
    name: str
    format: str
    userName:str
    pages:list[Page] = []
    create_date: datetime = datetime.today()

class User(BaseModel):
    user_name:str
    password:str

