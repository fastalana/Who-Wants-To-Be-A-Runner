import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import app, db, create_app
from models import setup_db, Athlete, Stat


# MEMBER USER GENERATED FOR TESTING PURPOSES ONLY
# HAS ALL PERMISSIONS: "get:all_athletes", "get:all_stats", "post:athlete", "post:stat", "patch:stat", "delete:stat"
MEMBER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhlbkxVTVBwNkFQR3FFNGVKeDVOaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYXY1ZHA0ZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OGI4YzIwZmI2YzYwYzgzYTQxZGJmIiwiYXVkIjoicnVubmVycyIsImlhdCI6MTU4NzEzNDU2NSwiZXhwIjoxNTg3MjIwOTY1LCJhenAiOiJVQ0hrank2RlJDb2lLU1R5bWpJQUtrTVFHckVvUjl1YyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnN0YXQiLCJnZXQ6YWxsX2F0aGxldGVzIiwiZ2V0OmFsbF9zdGF0cyIsInBhdGNoOnN0YXQiLCJwb3N0OmF0aGxldGUiLCJwb3N0OnN0YXQiXX0.MVbc4lJqskIuupBApkDG8cGcA_pWGdt5eyrJ2K0eQp5I4x5T-F1o3GomBEMFumlPSXBEE2I1E1Ks-SHIGTJ9eC8BqF8wFgLC4LlCLTO3tRjIxt5rKJeWhrFACX5Ss8lcxNrr7sCuuMmg9OD9LAah0bTOM9Y_yF5e6qLYf4ZQ5dR2ORsu3YWvwcbS4PV1aRUg58-6W6JscH3sU61gvF53gv0rTyqSa1WJfX1lmOIolw_lNwVFAWMgC4aFAWM-JXHA5pBcT-FXwpChNWm-DXWY1SgispwHTt-f7afg3VEbHeHupVAzV0Jaryj8Y0vPkt-97aGDiwwQUa_vUt6psMOJHA'

# PUBLIC USER GENERATED FOR TESTING PURPOSED ONLY
# HAS NO PERMISSIONS
PUBLIC_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhlbkxVTVBwNkFQR3FFNGVKeDVOaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYXY1ZHA0ZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OWNkYjg5NjA3MTEwYzllY2U3ZDNjIiwiYXVkIjoicnVubmVycyIsImlhdCI6MTU4NzEzODA0MCwiZXhwIjoxNTg3MjI0NDQwLCJhenAiOiJVQ0hrank2RlJDb2lLU1R5bWpJQUtrTVFHckVvUjl1YyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.LnhMw1XzfJynYvN_S9s40kjBGmphQ0kD1knWsObap6p79CWK1q2LXb7ZBehX3yph2vLSh5fO53oImgLmtetziT5e-nEMBsxk2EHxX4yAjmN2rXJ3wsp0eAWQNEBuk3lOE2LjDBEE3YsfToHlStS0ktD0Ecei-h8-Ct-yrSsUicfqw1uyW2ETnthCPhI_yfa9TO5rb5bk_S5g_RPDf56P7FzhByeb5EpsmgkXyIpzROykO7VNptAThM3RnwXmQ1PxKJ4nA7Sqan1w8VjFLANrtgZQXoNX65wDnG9QbMDzBYqFdm5fnUzVO7fbP_fhsF9I_YXtMNbjrP8vRrTlROsPQg'
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
    def test_get_athletes_member(self):
        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.get('/athletes', headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_athletes_public(self):
        self.headers.update({'Authorization': 'Bearer ' + PUBLIC_TOKEN})
        response = self.client.get('/athletes', headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_get_stats_member(self):
        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.get('/stats', headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_stats_public(self):
        response = self.client.get('/stats')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)
    
    # PUT ENDPOINTS
    def test_add_athlete_member(self):
        new_athlete = {
            "first_name": "Amelia",
            "last_name": "Boone"
        }

        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.post('/athletes', json=new_athlete, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_athlete_public(self):
        new_athlete = {
            "first_name": "Amelia",
            "last_name": "Boone"
        }

        response = self.client.post('/athletes', json=new_athlete)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_add_stat_member(self):
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

        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.post('/stats', json=new_stat, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_stat_public(self):
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
        # self.assertEqual(response.status_code, 401)

    # PATCH ENDPOINT
    def test_update_stat_member(self):
        updated_stat = {
            "athlete_id":"1"
        }

        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.patch('/stats/1', json=updated_stat, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_update_stat_public(self):
        updated_stat = {
            "athlete_id":"1"
        }

        response = self.client.patch('/stats/1', json=updated_stat)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    # DELETE ENDPOINT
    def test_delete_stat_member(self):
        self.headers.update({'Authorization': 'Bearer ' + MEMBER_TOKEN})
        response = self.client.patch('/stats/1', headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_delete_stat_public(self):
        response = self.client.patch('/stats/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

# Make the tests conviently executable
if __name__ == "__main__":
    unittest.main()