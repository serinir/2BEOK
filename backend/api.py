from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.diagnose import Diagnose
from backend.login import Login
from backend.signup import Signup
from backend.tickets import Tickets
from backend.doctor import Doctor
from json import loads

app = Flask(__name__)
cors = CORS(app)
jwt = JWTManager(app)
api = Api(app)
# api = swagger.docs(api, apiVersion='0.1', api_spec_url='/api/spec')
app.config["JWT_SECRET_KEY"] = "yellow submarine"
app.config["PROPAGATE_EXCEPTIONS"] = True

api.add_resource(Login, "/api/login")
api.add_resource(Signup, "/api/signup")
api.add_resource(Tickets, "/api/tickets")
api.add_resource(Doctor, "/api/doctor")
api.add_resource(Diagnose, "/api/diagnose")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)