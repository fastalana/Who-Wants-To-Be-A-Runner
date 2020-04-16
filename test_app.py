import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import app, db, create_app
from models import setup_db, Athlete, Stat


# USER GENERATED FOR TESTING PURPOSES ONLY
# HAS PERMISSIONS: "get:requests", "post:requests", "patch:requests", "delete:requests", 
MEMBER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhlbkxVTVBwNkFQR3FFNGVKeDVOaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYXY1ZHA0ZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OGI4YzIwZmI2YzYwYzgzYTQxZGJmIiwiYXVkIjoicnVubmVycyIsImlhdCI6MTU4NzA2NzI2NywiZXhwIjoxNTg3MTUzNjY3LCJhenAiOiJVQ0hrank2RlJDb2lLU1R5bWpJQUtrTVFHckVvUjl1YyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnJlcXVlc3RzIiwiZ2V0OnJlcXVlc3RzIiwicGF0Y2g6cmVxdWVzdHMiLCJwb3N0OnJlcXVlc3RzIl19.eY5WNecE6rNQNp9otUFUZ1EncLc2YQpfHWSp330HDmWsAGa7vGXKhKarxNLPaq121ov07Rr6IAtD-VswcW1jQX65wuKqn51TDr-0LZlj0r-xg40Bgq8kV3FN9grKKM7NnmLRVTic8ALjp1q_VBWWRwPINIeBqWyou218cjk6qmXF_cszd8TO7lboiMdaoBq_BHg0Jrf_321udIBfwSQ-YW6XXV7ib1HFituj5cb8n3aFDlvz_5bbnoCpinyks_Um-nyOmF2NyDaeYicUFpGcUzcNbhbzf9QgjLI2OfaoLteuoBWzdkoAT0uIs8ldqrefAblybUW3bfOhJ2XA9Vvr1A'

class RunnerTestCase(unittest.TestCase):
    
    def setUp(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://alanabellucci@localhost:5432/runners_test'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.client = app.test_client()
        self.headers = {'Content-Type': 'application/json'}
        
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Execute after each test
        pass

    # GET ENDPOINTS
    def test_get_athletes(self):
        response = self.client.get('/athletes')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_stats(self):
        response = self.client.get('/stats')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
    
    # PUT ENDPOINTS
    def test_add_athlete(self):
        new_athlete = {
            "first_name": "Amelia",
            "last_name": "Boone"
        }

        response = self.client.post('/athletes', json=new_athlete)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_stat(self):
        new_stat = {
            "athlete_id":"1", 
            "avg_miles_per_week":"2", 
            "avg_vertical_per_week":"3", 
            "longest_run":"4", 
            "longest_run_2_weeks":"5", 
            "race_distance":"6", 
            "race_veritcal":"7", 
            "race_date":"2020-08-09"
        }

        response = self.client.post('/stats', json=new_stat)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    # PATCH ENDPOINT
    def test_update_stat(self):
        updated_stat = {
            "athlete_id":"1"
        }

        response = self.client.patch('/stats/1', json=updated_stat)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    # DELETE ENDPOINT
    def test_delete_stat(self):

        response = self.client.patch('/stats/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

# Make the tests conviently executable
if __name__ == "__main__":
    unittest.main()