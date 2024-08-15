from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


class Page(BaseModel):
    name: str
    content: str
    diary_id: str
    date: str


class Diary(BaseModel):
    name: str
    format: str
    user_id: str
    create_date: datetime = datetime.today()


class User(BaseModel):
    username: str
    password: str
