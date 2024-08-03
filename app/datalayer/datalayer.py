from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..classes.classes import Diary, User
import re


class mongo:
    uri = "mongodb+srv://alon8070:hV9PHw0w6tmnICeE@cluster0.hh2b0ve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    db_name = "food-diary"
    client = MongoClient(uri, server_api=ServerApi("1"))
    db = client[db_name]
    def __init__(self) -> None:
        try:            
            self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Init Mongo Error!: ")
            print(e)

    def add_diary(self, diary:Diary):
        diary_collection = "diarys"
        dict_diary = diary.model_dump()
        try:
            self.db[diary_collection].insert_one(dict_diary)
        except Exception as e:
            print("Add Diary Document Error!: ")
            print(e)
            
    def check_username(self, user_name:str):
        user_collection = "users"
        try:
            user = self.db[user_collection].find_one({"user_name":user_name},{"_id":0,"password":0})
            return user is not None
        except Exception as e:
            print("Is Username Valid Error!: ")
            print(e)
                        
    def add_user(self, user:User):
        user_collection = "users"
        dict_user = user.model_dump()
        try:
            if(self.is_username_valid(user)):                
                self.db[user_collection].insert_one(dict_user)
                return True
            else:
                return False
        except Exception as e:
            print("Add User Document Error!: ")
            print(e)
            
            
    def get_all_users(self):
        user_collection = "users"
        try:
            users = list(self.db[user_collection].find({},{"user_name":1, "_id":0}))
            print(users)
            return users
        except Exception as e:
            print(e)
        
   
            

    