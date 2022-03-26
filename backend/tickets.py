from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
from datetime import datetime
from utility import check_args
from bson.objectid import ObjectId
from database.db_api import db


class Tickets(Resource):

    put_args = [
        'patient_id',
        'doctor_id'
    ]

    def get(self):
        data = request.get_json()

        ticket = db.tickets().get_ticket(_id=ObjectId(data['_id']))

        patient = db.users().get_user(_id=ticket['patient'])
        ticket['patient'] = {'first_name': patient['first_name'], 'last_name': patient['last_name'], 'mail': patient['mail']}
        ticket['doctors'] = [i.binary.hex() for i in ticket['doctors']]

        return ticket, 200

    def put(self):
        # Create a new ticket when a patient selects the timeslot of the doctor
        if not check_args(request.get_json(), *self.put_args):
            return "Missing Arguments", 400

        data = request.get_json()

        ticket = {
            'doctors': [ObjectId(data['doctor_id'])],
            'patient': ObjectId(data['patient_id']),
            'history': []
        }

        res = db.tickets().insert_ticket(ticket)

        db.users().update_user(doctor_id=ObjectId(data['doctor_id']), ticket_id=res.inserted_id)


        return {'_id': res.inserted_id.binary.hex()}, 200

    def post(self):
        # Add a new doctor to the ticket or add a note to the ticket' history

        data = request.get_json()

        if 'doctor_id' in data.keys():
            db.tickets().update_ticket(_id=data['_id'], doctor_id=data['doctor_id'])
            db.users().update_user(doctor_id=ObjectId(data['doctor_id']), ticket_id=data['_id'])
        elif 'summary' in data.keys():
            data['date'] = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
            db.tickets().update_ticket(_id=data['_id'], summary=data['summary'])

        return '', 200