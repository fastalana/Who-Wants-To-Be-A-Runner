import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import app, db, create_app
from models import setup_db, Athlete, Stat


# MEMBER USER GENERATED FOR TESTING PURPOSES ONLY
# HAS ALL PERMISSIONS:
# "get:all_athletes", "get:all_stats",
# "post:athlete", "post:stat", "patch:stat", "delete:stat"
MEMBER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhlbkxVTVBwNkFQR3FFNGVKeDVOaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYXY1ZHA0ZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OGI4YzIwZmI2YzYwYzgzYTQxZGJmIiwiYXVkIjoicnVubmVycyIsImlhdCI6MTU4NzIyODAyNSwiZXhwIjoxNTg3MzE0NDI1LCJhenAiOiJVQ0hrank2RlJDb2lLU1R5bWpJQUtrTVFHckVvUjl1YyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnN0YXQiLCJnZXQ6YWxsX2F0aGxldGVzIiwiZ2V0OmFsbF9zdGF0cyIsInBhdGNoOnN0YXQiLCJwb3N0OmF0aGxldGUiLCJwb3N0OnN0YXQiXX0.cWdbRVe2khLIKwQSDyrJ3wRlnPkr93eh9LMHxahTnd8DVCP2RnS4A5oJL37erYFK14BLfuKYdpmLnSLanR6yhTqlT0bzMObhEV45NmhaAZ2aAF7HA3cfdcNJ1TRIwIGd7KabP0Qi3_SFKHClDu-FFFWH1XFTiB81I4BCeSIs0zpnpXirYjuZY2maW2J8siO0tvWZUqWnJ0psUtt9B7hP39KGayVFiWFYCmgwcszWAkHUPqNZKWJAGj3YtytcxDpIR2xnQ7Q0H89Hs2yskeY-zKJNGdUxxmbLIR0BQ3FH-5c8NvAa70Cu891jhglTvyGPekNj3M11Y6q_mcz35rvmcw'

# PUBLIC USER GENERATED FOR TESTING PURPOSED ONLY
# HAS NO PERMISSIONS
PUBLIC_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhlbkxVTVBwNkFQR3FFNGVKeDVOaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYXY1ZHA0ZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OWNkYjg5NjA3MTEwYzllY2U3ZDNjIiwiYXVkIjoicnVubmVycyIsImlhdCI6MTU4NzIyODA4MiwiZXhwIjoxNTg3MzE0NDgyLCJhenAiOiJVQ0hrank2RlJDb2lLU1R5bWpJQUtrTVFHckVvUjl1YyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.UMyFC77QER9CcZYr3HtruNHnSJUw7ps496sa1fjHpqtpLdxB00gpUjuM-42dJeYUldrpMU30OVeqSqGQr48MdsX_qsN7wZoAM80QbT_zTf2PwCtQ2B_NhqcSMXvX76HX8FsCQATr5AkpSi9-DmRdHuPtJwdIJ9Qt03FY69Kp5rCrTGsevdJIleM8pmEemHa8sKnI6JyOsS0OOwRY234q7lBwCM_u72_UwQib5sDyYB3tfLY5n87-dv5O85KXRZl7_JSJtgiPS5hSt-Lm_9Ta7Xhl5rP4rm6Afjsc47mQQAb5WpD5XmyDdsqEnRLQ_E1UHREZQv5IE2yHXXYimGG8MA'


class RunnerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://alanabellucci@localhost:5432/runners_test'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.client = app.test_client()
        self.headers_member = {
            'Content-Type': 'application/json',
            'Authorization': MEMBER_TOKEN}
        self.headers_public = {
            'Content-Type': 'application/json',
            'Authorization': PUBLIC_TOKEN}

        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Execute after each test
        pass

    # GET ENDPOINTS
    def test_get_athletes_member(self):
        response = self.client.get(
            '/athletes',
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_athletes_public(self):
        response = self.client.get(
            '/athletes',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_get_stats_member(self):
        response = self.client.get(
            '/stats',
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_stats_public(self):
        response = self.client.get(
            '/stats',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    # PUT ENDPOINTS
    def test_add_athlete_member(self):
        new_athlete = {
            "first_name": "Amelia",
            "last_name": "Boone"
        }

        response = self.client.post(
            '/athletes',
            json=new_athlete,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_athlete_public(self):
        new_athlete = {
            "first_name": "Amelia",
            "last_name": "Boone"
        }

        response = self.client.post(
            '/athletes',
            json=new_athlete,
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_add_stat_member(self):
        new_stat = {
            "athlete_id": "1",
            "avg_miles_per_week": "2",
            "avg_vertical_per_week": "3",
            "longest_run": "4",
            "longest_run_2_weeks": "5",
            "race_distance": "6",
            "race_veritcal": "7",
            "race_date": "2020-08-09"
        }

        response = self.client.post(
            '/stats',
            json=new_stat,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_stat_public(self):
        new_stat = {
            "athlete_id": "1",
            "avg_miles_per_week": "2",
            "avg_vertical_per_week": "3",
            "longest_run": "4",
            "longest_run_2_weeks": "5",
            "race_distance": "6",
            "race_veritcal": "7",
            "race_date": "2020-08-09"
        }

        response = self.client.post(
            '/stats',
            json=new_stat,
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    # PATCH ENDPOINT
    def test_update_stat_member(self):
        updated_stat = {
            "athlete_id": "1"
        }

        response = self.client.patch(
            '/stats/1',
            json=updated_stat,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_update_stat_public(self):
        updated_stat = {
            "athlete_id": "1"
        }

        response = self.client.patch('/stats/1', json=updated_stat)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    # DELETE ENDPOINT
    def test_delete_stat_member(self):
        response = self.client.patch('/stats/1', headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_delete_stat_public(self):
        response = self.client.patch(
            '/stats/1',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)


# Make the tests conviently executable
if __name__ == "__main__":
    unittest.main()
