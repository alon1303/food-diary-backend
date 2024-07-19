from fastapi import APIRouter
from ..classes.classes import Diary
from ..datalayer.datalayer import mongo
get_router = APIRouter()

db = mongo()

@get_router.get('/users/get-all-users')
def get_all_users():
    try:        
        return db.get_all_users()
    except Exception as e:
        print(e)
    
    
