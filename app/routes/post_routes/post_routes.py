from fastapi import APIRouter
from ...classes.diary import Diary
from ...datalayer.datalayer import mongo
post_router = APIRouter()

db = mongo()
@post_router.post("/add-diary")
def add_diary(diary):
    try:        
        db.add_diary(diary)
    except Exception as e:
        print(e)
        
        
