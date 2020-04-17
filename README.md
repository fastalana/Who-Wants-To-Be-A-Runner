# Who Wants To Be A Runner?

## About
This is the capstone project for Udacity's Full Stack Web Development Nanodegree.  The project provides the backbone to create a running training plan or mid-season check-in for runners.  At a future stage, athletes will be given a UI where they can enter their info and receive a training plan.

* https://who-wants-to-be-a-runner.herokuapp.com/

## API
In order to use the API users need to be authenticated. 
Users can either have a athlete or a coach role. An overview of the API can be found below as well.  We've also provided a [Postman Collection](https://github.com/fastalana/WhoWantsToBeARunner/blob/master/who-wants-to-be-a-runner.postman_collection.json).

### Roles and Permissions 
#### Coaches 
_Coaches can retrieve all information about athletes and all of their stats._

They have the following permissions:
* get:all_athletes
* get:all_stats

#### Athletes 
_Athletes can create an athlete and manage their stats through CRUD operations._

They have the following permissions:
* post:athlete
* post:stat
* patch:stat
* delete:stat


**Outlined below are examples of each of the API endpoints:**


### Retreiving data (Coaches only)

**GET** `/athletes`

Retrieves a list of all athletes

```
curl -X GET \
  https://who-wants-to-be-a-runner.herokuapp.com/athletes \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'
```

**GET** `/stats`

Retrieves a list of stats

```
curl -X GET \
  https://who-wants-to-be-a-runner.herokuapp.com/stats \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'
```

### Managing data (Athletes only)

**POST** `/athletes`

Add a new athlete

```
curl -X POST \
  https://who-wants-to-be-a-runner.herokuapp.com/athletes \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
        "first_name":"Deena", 
        "last_name":"Kastor"
}'
```

**POST** `/stats`

Add a new stat

```
curl -X POST \
  https://who-wants-to-be-a-runner.herokuapp.com/stats \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
        "athlete_id":"1", 
        "avg_miles_per_week":"2", 
        "avg_vertical_per_week":"3", 
        "longest_run":"4", 
        "longest_run_2_weeks":"5", 
        "race_distance":"6", 
        "race_veritcal":"7", 
        "race_date":"2020-08-09"
}'
```

**PATCH** `/stats/<id>`

Change information for a stat

```
curl -X PATCH \
  https://who-wants-to-be-a-runner.herokuapp.com/stats/1 \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "athlete_id":"5"
}'
```

**DELETE** `/stats/<id>`

Delete a stat

```
curl -X DELETE \
  https://who-wants-to-be-a-runner.herokuapp.com/stats/1 \
  -H 'Authorization: Bearer <INSERT_YOUR_TOKEN> ' \

```

## Installation

The following section explains how to set up and run the project locally.

### Installing Dependencies

The project requires Python 3.6. Using a virtual environment is recommended. Set up the project as follows:

```

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

```

### Database Setup

With Postgres running, create a database:

```

createdb runners

```

### Running the server

To run the server, first set the environment variables, then run:

```bash
export FLASK_APP=app.py
flask run

```

## Testing

To test the API, first create a test database in postgres and then execute the tests as follows:

```
createdb test_runners
python3 test_app.py
```