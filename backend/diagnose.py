from flask import request
from flask_restful import Resource
from predict import predict
import random


class Diagnose(Resource):

    def post(self):
        
        return {"probability": random.choice(predict()[:,2])}, 200