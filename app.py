from flask import Blueprint
from flask_restful import Api
from resources.Reminder import ReminderResource
from resources.User import UserResource
from resources.Location import LocationResource
from resources.Scheduled import ScheduledResource
from resources.UserId import UserIdResource
from resources.UsersReminder import UsersReminderResource
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/mediminderx_be"
db = SQLAlchemy(app)

from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
@app.route('/')
def index():
    return 'Hello'
api.add_resource(ReminderResource, '/reminders')
api.add_resource(UserResource, '/users')
api.add_resource(LocationResource, '/locations')
api.add_resource(ScheduledResource, '/scheduled')
api.add_resource(UserIdResource, '/users/<int:id>')
api.add_resource(UsersReminderResource, '/users/<int:user_id>/reminders')

from Model import db
db.init_app(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
