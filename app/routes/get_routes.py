from fastapi import APIRouter
from ..classes.classes import Diary, User
from ..datalayer.datalayer import mongo

get_router = APIRouter()

db = mongo()

@get_router.get('/users/get-all-users')
def get_all_users():
    try:        
        return db.get_all_users()
    except Exception as e:
        print(e)
    
@get_router.get('/users/check-username/{username}')
def check_username(username:str):
    try:
               
        return db.check_username(username)
    except Exception as e:
        print(e)
    
@get_router.get('/users/login')
def login(user_name:str, password:str):
    try:               
        return db.login(user_name, password)
    except Exception as e:
        print(e)
        
@get_router.get('/users/get-user-id')
def get_user_id(username:str):
    try:
        return db.get_user_id(username)
    except Exception as e:
        print(e)
@get_router.get('/diarys/get-diarys-by-user-id')
def get_diarys_by_user_id(user_id:str):
    try:
        return db.get_diarys_by_user_id(user_id)
    except Exception as e:
        print(e)
@get_router.get('/pages/get-pages-by-diary-id')
def get_pages_by_diary_id(diary_id:str):
    try:
        return db.get_pages_by_diary_id(diary_id)
    except Exception as e:
        print(e)
