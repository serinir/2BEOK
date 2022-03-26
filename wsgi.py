from flask import appcontext_popped
from flask_restful import Api
from api import app


if __name__ == "__main__":
    app.run()