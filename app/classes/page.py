from pydantic import BaseModel

class Page(BaseModel):
    name:str
    content:str
    date:str