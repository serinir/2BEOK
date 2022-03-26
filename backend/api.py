from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from diagnose import Diagnose
from login import Login
from signup import Signup
from tickets import Tickets
from doctor import Doctor
from json import loads


app = Flask(__name__)
cors = CORS(app)
jwt = JWTManager(app)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "yellow submarine"
app.config["PROPAGATE_EXCEPTIONS"] = True

api.add_resource(Login, "/api/login")
api.add_resource(Signup, "/api/signup")
api.add_resource(Tickets, "/api/tickets")
api.add_resource(Doctor, "/api/doctor")
api.add_resource(Diagnose, "/api/diagnose")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)