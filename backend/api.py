from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from login import Login
from signup import Signup
from tickets import Tickets
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

# doctor 623ec7fa99f3223b7bf40f83, 623ec80a99f3223b7bf40f84
# patient 623ec82799f3223b7bf40f85
# ticket 623ec84699f3223b7bf40f86
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)