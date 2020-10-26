from flask import request
from flask_restful import Resource
from Model import db, Reminder, ReminderSchema

reminders_schema = ReminderSchema(many=True)
reminder_schema = ReminderSchema()

class ReminderResource(Resource):
    def get(self):
        reminders = Reminder.query.all()
        reminders = reminders_schema.dump(reminders)
        return {'status': 'success', 'data': reminders}, 200

    def post(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = reminder_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #         reminder = Reminder.query.filter_by(name=data['name']).first()
    #     if reminder:
    #         return {'message': 'Reminder already exists'}, 400

        reminder = Reminder(name=json_data['name'], user_id=json_data['user_id'], supplies=json_data['supplies'], days=json_data['days'], time=json_data['time'], show_supplies=json_data['show_supplies'], full_date=json_data['full_date'])

        db.session.add(reminder)
        db.session.commit()
        result = reminder_schema.dump(reminder)
        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = reminder_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #         reminder = Reminder.query.filter_by(id=data['id']).first()
    #     if not reminder:
    #         return {'message': 'Reminder does not exist'}, 400
        reminder = Reminder.query.filter_by(id=json_data['id']).first()
        reminder.supplies=json_data['supplies']
        reminder.days=json_data['days']
        reminder.time=json_data['time']
        reminder.show_supplies=json_data['show_supplies']
        reminder.name = json_data['name']
        reminder.full_date = json_data['full_date']
        db.session.commit()
        result = reminder_schema.dump(reminder)
        return { "status": 'success', 'data': result }, 200

    def delete(self):
        json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    #     data, errors = reminder_schema.load(json_data)
    #     if errors:
    #         return errors, 422

        reminder = Reminder.query.filter_by(id=json_data['id']).delete()
        db.session.commit()
        result = reminder_schema.dump(reminder)
        return { "status": 'success', 'message': 'Reminder sucessfully deleted'}, 200
