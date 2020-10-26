from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Reminder import ReminderResource
from resources.User import UserResource, UserIdResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello', '/Hello/<int:id>')
api.add_resource(ReminderResource, '/Reminder')
api.add_resource(UserResource, '/User')
api.add_resource(UserIdResource, '/User/<int:id>')

