from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

# database_path = os.environ['DATABASE_URL']
database_path = 'postgres://alanabellucci@localhost:5432/herokutest'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()

class Athlete(db.Model):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def athlete_to_dictionary(self):
        return{
            'id': self.id,
            'first name': self.first_name,
            'last name': self.last_name
        }

    def __repr__(self):
        return f'<Athlete Id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}>'