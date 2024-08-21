from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..classes.classes import Diary, User, Page
import re
from bson import ObjectId


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

    ######################################
    # Should Be Put!!!!!!!!!!!!!!!!!!!!!!!
    ######################################

    def check_username(self, user_name: str):

        user_collection = self.db["users"]
        try:
            user = user_collection.find_one(
                {"user_name": user_name}, {"_id": 0, "password": 0}
            )
            return user is not None
        except Exception as e:
            print("Is Username Valid Error!: ")
            print(e)

    def login(self, user_name: str, password: str):
        user_collection = self.db["users"]
        try:
            user_fetch = user_collection.find_one(
                {"user_name": user_name, "password": password}, {"_id": 0}
            )
            return user_fetch is not None
        except Exception as e:
            print(e)

    ######################################
    # Get Functions!!!!!!!!!!!!!!!!!!!!!!!
    ######################################

    def get_user_id(self, username: str):
        user_collection = self.db["users"]
        try:
            user_fetch = user_collection.find_one(
                {"user_name": username}, {"user_name": 0, "password": 0}
            )
            user_id = str(user_fetch["_id"])
            return user_id

        except Exception as e:
            print("Get User Id Error!: ")
            print(e)

    def get_diarys_by_user_id(self, user_id: str):
        diarys_collection = self.db["diarys"]
        try:
            fetch_diarys = diarys_collection.find({"user_id": user_id})
            dict_diarys = list(fetch_diarys)
            return dict_diarys
        except Exception as e:
            print("Get Diarys By user id Error!: ")
            print(e)

    def get_pages_by_diary_id(self, diary_id: str):
        pages_collection = self.db["pages"]
        try:
            fetch_pages = pages_collection.find({"diary_id": diary_id})
            dict_pages = list(fetch_pages)
            return dict_pages
        except Exception as e:
            print("Get pages By diarys id Error!: ")
            print(e)

    ######################################
    # Add Functions!!!!!!!!!!!!!!!!!!!!!!!
    ######################################

    def add_page(self, page: Page):
        pages_collection = self.db["pages"]
        try:
            pages_collection.insert_one(page)
        except Exception as e:
            print("Add Page Document Error!: ")
            print(e)

    def add_diary(self, diary: Diary):
        diary_collection = self.db["diarys"]
        dict_diary = diary.model_dump()
        try:
            diary_collection.insert_one(dict_diary)
        except Exception as e:
            print("Add Diary Document Error!: ")
            print(e)

    def add_user(self, user: User):

        user_collection = self.db["users"]
        dict_user = user.model_dump()
        try:
            user_collection.insert_one(dict_user)

        except Exception as e:
            print("Add User Document Error!: ")
            print(e)
