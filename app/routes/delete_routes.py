from fastapi import APIRouter
from ..classes.classes import Diary, User
from ..datalayer.datalayer import mongo

delete_router = APIRouter()

db = mongo()

@delete_router.delete('/diarys/delete-diarys-by-user-id')
def delete_diarys(user_id:str):
    try:
        db.delete_diarys(user_id)
    except Exception as e:
        print("delete diarys route error!: " , e)
        
        

        
@delete_router.delete('/diarys/delete-diary-by-id')
def delete_diary(diary_id:str):
    try:
        return db.delete_diary(diary_id)
    except Exception as e:
        print("delete diary by id route error!: ", e)