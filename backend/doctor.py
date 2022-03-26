from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
from bson.objectid import ObjectId
from backend.database.db_api import db


def check_if_doctor(f):

    def wrapper(*args):
        verify_jwt_in_request()
        _id = ObjectId(get_jwt_identity())
        claims = get_jwt()

        res = db.users().get_user(_id=_id)
        try:
            if not claims['is_doctor'] or not res['is_doctor']:
                return {'auth': False}, 401
        except Exception:
            return {'auth': False}, 401

        return f(*args)

    return wrapper


class Doctor(Resource):
 
    @check_if_doctor
    def get(self):
        ids = db.users().get_user(_id=ObjectId(get_jwt_identity()))['tickets']

        tickets = db.tickets().get_tickets(ids=ids)

        for ticket in tickets:
            patient = db.users().get_user(_id=ticket['patient'])
            ticket['doctors'] = [i.binary.hex() for i in ticket['doctors']]
            ticket['patient'] = {'first_name': patient['first_name'], 'last_name': patient['last_name'], 'mail': patient['mail']}

        return tickets, 200