from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Reminder import ReminderResource
from resources.User import UserResource
from resources.UserId import UserId
from resources.UserReminder import UserReminder

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
# api.add_resource(Hello, '/hello', '/hello/<int:id>')
api.add_resource(ReminderResource, '/reminders')
api.add_resource(UserResource, '/users')
api.add_resource(UserId, '/users/<int:id>')
api.add_resource(UserReminder, '/users/<int:user_id>/reminders')

