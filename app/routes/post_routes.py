from fastapi import APIRouter
from ..classes.classes import Diary, User,Page
from ..datalayer.datalayer import mongo
post_router = APIRouter()

db = mongo()

@post_router.post("/diarys/add-diary")
def add_diary(diary: Diary):
    try:        
        db.add_diary(diary)
    except Exception as e:
        print(e)

    

@post_router.post("/users/add-user")
def add_user(user: User):
    try:
        db.add_user(user)
    except Exception as e:
        print(e)
        
@post_router.post("/pages/add-page")
def add_page(page:Page):
    try:
        db.add_page(page)
    except Exception as e:
        print(e)


        
