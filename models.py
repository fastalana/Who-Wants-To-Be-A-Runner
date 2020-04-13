from sqlalchemy import (
    Column, 
    create_engine,
    Date,
    ForeignKey,
    Integer, 
    String)  
from flask_sqlalchemy import SQLAlchemy
import json
import os

# database_path = os.environ['DATABASE_URL']
database_path = 'postgres://alanabellucci@localhost:5432/runners'

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

    # stat = db.relationship('Athlete', secondary = 'stats')

    def athlete_to_dictionary(self):
        return{
            'id': self.id,
            'first name': self.first_name,
            'last name': self.last_name
        }

    def __repr__(self):
        return f'<Athlete Id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}>'

class Stat(db.Model):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'), primary_key=True)
    avg_miles_per_week = Column(Integer)
    avg_vertical_per_week = Column(Integer)
    longest_run = Column(Integer)
    longest_run_2_weeks = Column(Integer)
    race_distance = Column(Integer)
    race_veritcal = Column(Integer)
    race_date = Column(Date)

    # athlete = db.relationship('Athlete') # allows us to call Athlete fields on Stat

    def stat_to_dictionary(self):
        return{
            'id': self.id,
            'athlete id': self.athlete_id,
            'average miles per week': self.avg_miles_per_week,
            'average vertical per week': self.avg_vertical_per_week,
            'longest run': self.longest_run,
            'longest run in the last two weeks': self.longest_run_2_weeks,
            'race distance': self.race_distance,
            'race vertical': self.race_veritcal,
            'race_date': self.race_date
        }

    def __repr__(self):
        return f'<Stat Id: {self.id}, Stat Athlete Id: {self.athlete_id}>'