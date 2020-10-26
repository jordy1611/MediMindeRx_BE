from flask import jsonify, request
from flask_restful import Resource
from Model import db, User, Reminder, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserReminder(Resource):
    def get(self, user_id):
        reminders = Reminder.query.filter_by(user_id = user_id)
        reminders = users_schema.dump(reminders)
        return {"status":"success", "data":reminders}, 200
