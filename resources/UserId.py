from flask import jsonify, request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserId(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id)
        user = users_schema.dump(user)
        # users = users_schema.dump(users)
        return {"status":"success", "data": user}, 200