from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    supplies = db.Column(db.String(250), nullable=False)
    days = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String(250), nullable=False)
    full_date = db.Column(db.Integer)
    show_supplies = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('reminders', lazy='dynamic' ))

    def __init__(self, name, user_id, supplies, days, time, show_supplies, full_date):
        self.name = name
        self.user_id = user_id
        self.supplies = supplies
        self.days = days
        self.time = time
        self.full_date = full_date
        self.show_supplies = show_supplies


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class ReminderSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    name = fields.String(required=True)
    supplies = fields.String(required=True)
    days = fields.String(required=True)
    time = fields.String(required=True)
    full_date = fields.Integer(required=True)
    show_supplies = fields.Boolean(required=True)
    creation_date = fields.DateTime()
