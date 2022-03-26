from hashlib import sha256
from datetime import datetime
from os import getenv
from bson.objectid import ObjectId

class Users():

    def __init__(self, db) -> None:
        self.users = db['users']
        self.SALT = "yellow submarine"

    def get_user(self, mail: str = None, password: str = None, _id: ObjectId = None) -> dict:
        try:
            if not _id:
                res = self.users.find_one({
                    "mail": mail,
                    "password": self.hash_pwd(password)
                })
            else:
                res = self.users.find_one({
                    "_id": _id
                })

            if res:
                    return res
        except Exception:
                return None

        return None

    def get_users(self) -> list:
        res = self.users.find({
            'is_resp': True
        })

        res = [{
            '_id': i['_id'].binary.hex(),
            'nom': i['nom'],
            'prenom': i['prenom'],
            'mail': i['mail']
        } for i in res]

        return sorted(res, key=lambda i: (i['nom'], i['prenom']))

    def insert_user(self, user: dict) -> dict:
        user['date'] = datetime.utcnow()
        user['password'] = self.hash_pwd(user['password'])
        return self.users.insert_one(user)

    def delete_user(self, _id: str) -> None:
        try:
            self.users.delete_one({
                "_id": ObjectId(_id)
            })
        except Exception:
            pass

    def update_user(self, doctor_id: ObjectId, ticket_id: ObjectId):
        tickets = self.get_user(_id=doctor_id)['tickets'] + [ticket_id]
        self.users.update_one({"_id": doctor_id}, {"$set": {"tickets": tickets}})

    def hash_pwd(self, password: str) -> bytes:
        r = self.SALT + password
        return sha256(r.encode()).digest()