from flask import request
from flask_restful import Resource
from backend.utility import check_args
from backend.database.db_api import db

class Signup(Resource):
    post_args = [
        "first_name",
        "last_name",
        "mail",
        "password",
        "is_doctor"
    ]

    def post(self):
        if not check_args(request.get_json(), *self.post_args):
            return "Missing Arguments", 400

        data = request.get_json()
        
        user = {i: data[i] for i in self.post_args}
        user['last_name'] = user['last_name'].upper()
        user['first_name'] = user['first_name'].capitalize()

        if not user['is_doctor']:
            user["form"] = data["form"]
        else:
            user['tickets'] = []

        res = db.users().insert_user(user)

        return {'_id': res.inserted_id.binary.hex()}, 200
