from flask import jsonify, request
from flask_restful import Resource
from Model import db, User, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users)
        return {"status":"success", "data":users}, 200

    def post(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = user_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #         user = User.query.filter_by(name=data['name']).first()
    #     if user:
    #         return {'message': 'User already exists'}, 400

        user = User(name=json_data['name'])

        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = user_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #         user = User.query.filter_by(id=data['id']).first()
    #     if not user:
    #         return {'message': 'User does not exist'}, 400

        user.name = json_data['name']
        db.session.commit()
        result = user_schema.dump(user)
        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = user_schema.load(json_data)
    #     if errors:
    #         return errors, 422

        user = User.query.filter_by(id=json_data['id']).delete()
        db.session.commit()
        result = user_schema.dump(user)
        return { "status": 'success', 'data': result}, 204
