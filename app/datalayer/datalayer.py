from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..classes.diary import Diary


class mongo:
    uri = "mongodb+srv://alon1303:Alon1303@food-diary.39ybefu.mongodb.net/?retryWrites=true&w=majority&appName=food-diary&authSource=admin"
    
    db_name = "food-diary"
    client = MongoClient(uri, server_api=ServerApi("1"))
    def __init__(self) -> None:
        try:            
            self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Init Mongo Error!: ")
            print(e)

    def add_diary(self, diary):
        diary_collection = "diarys"
        try:
            self.client[self.db_name][diary_collection].insert_one(diary)
        except Exception as e:
            print("Add Diary Document Error!: ")
            print(e)
