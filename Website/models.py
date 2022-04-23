
from Website import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    #foreign key connectivity
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#defining the schema for the object user
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    #tell the sql alchemy to add the note id and note to the user table
    notes = db.relationship('Note')









