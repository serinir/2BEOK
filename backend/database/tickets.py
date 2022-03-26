from hashlib import sha256
from datetime import datetime
from os import getenv
from bson.objectid import ObjectId

"""
_id: ObjectId
doctors: [ObjectId]
patient: ObjectId
history: [{doctor, summary, date}]
date: datetime
"""

class Tickets():

    def __init__(self, db) -> None:
        self.tickets = db['tickets']
        self.SALT = "yellow submarine"

    def get_ticket(self, _id: ObjectId) -> dict:
        res = self.tickets.find_one({
            "_id": _id
        })

        res = {
            '_id': res['_id'].binary.hex(),
            'doctors': res['doctors'],
            'patient': res['patient'],
            'history': res['history'],
            'date': res['date'].strftime("%Y/%m/%d %H:%M:%S")
        }

        return res

    def get_tickets(self, ids: list) -> list:
        res = [self.get_ticket(_id=i) for i in ids]

        return res

    def insert_ticket(self, ticket: dict) -> dict:
        ticket['date'] = datetime.utcnow()
        return self.tickets.insert_one(ticket)

    def update_ticket(self, _id: str, doctor_id: str = None, summary: dict = None):
        _id = ObjectId(_id)

        if doctor_id:
            doctors = self.get_ticket(_id=_id)['doctors'] + [ObjectId(doctor_id)]
            self.tickets.update_one({'_id': _id}, {"$set": {"doctors": doctors}})

        elif summary:
            history = self.get_ticket(_id=_id)['history'] + [summary]
            self.tickets.update_one({'_id': _id}, {"$set": {"history": history}})