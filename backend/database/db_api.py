import pymongo
from backend.database.users import Users
from backend.database.tickets import Tickets


class DB_Api():

    def __init__(self, host: str, user: str, password: str) -> None:
        self.client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}/myFirstDatabase?retryWrites=true&w=majority")
        
        self.db = self.client["depression-not"]

    def users(self) -> Users:
        return Users(self.db)

    def tickets(self) -> Tickets:
        return Tickets(self.db)


db = DB_Api("2beokhackandheal.u9gto.mongodb.net", "admin", "admin")