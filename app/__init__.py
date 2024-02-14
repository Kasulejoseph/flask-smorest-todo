from flask import Flask
from flask_smorest import Api

from app.config import APIConfig
from app.resources.task import todo

server = Flask(__name__)

server.config.from_object(APIConfig)
app = Api(server)
app.register_blueprint(todo)
