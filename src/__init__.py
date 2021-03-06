# src/__init__.py

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config.from_object('src.config.DevelopmentConfig')


class Ping(Resource):

    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


# app.add_url_rule('/', Ping)
api.add_resource(Ping, '/ping')
