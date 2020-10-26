from flask import request
from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "no id"}

    def get(self, id):
        return {"message": id}

    def post(self):
        return {"message": "Hello, World!"}
