import pymongo
from database.users import Users
from database.tickets import Tickets


class DB_Api():

    def __init__(self, host: str, user: str, password: str) -> None:
        self.client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:27017/")
        
        self.db = self.client["depression-not"]

    def users(self) -> Users:
        return Users(self.db)

    def tickets(self) -> Tickets:
        return Tickets(self.db)


db = DB_Api("localhost", "admin", "admin")