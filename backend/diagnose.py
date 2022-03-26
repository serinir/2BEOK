from flask import request
from flask_restful import Resource
from backend.predict import predict
import random


class Diagnose(Resource):

    def post(self):
        prc = random.choice(predict()[:,2]) * 100
        prc = f"{prc:.2f}"
        return {"probability": prc}, 200