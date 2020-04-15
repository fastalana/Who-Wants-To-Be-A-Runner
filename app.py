import os
from flask import Flask, request, abort, jsonify
from models import setup_db, db, Athlete, Stat
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/athletes')
    def get_athletes():
        athletes = Athlete.query.order_by(Athlete.last_name).all()

        return jsonify({
            'success': True,
            'athletes': [athlete.athlete_to_dictionary() for athlete in athletes],
            'total_athletes': len(athletes)
        })

    @app.route('/stats')
    def get_stats():
        stats = Stat.query.order_by(Stat.athlete_id).all()

        return jsonify({
            'success': True,
            'athletes': [stat.stat_to_dictionary() for stat in stats],
            'total_athletes': len(stats)
        })

    @app.route('/athletes', methods=['POST'])
    def create_athlete():
        body = request.get_json()

        first_name = body.get('first_name', None)
        last_name = body.get('last_name', None)

        if not ('first_name' in body and 'last_name' in body):
            abort(404)

        try:
            athlete = Athlete(first_name=first_name, last_name=last_name)
            db.session.add(athlete)
            db.session.commit()

            return jsonify({
                'success': True,
                'created athlete_id': athlete.id,
                'total_athlete': len(Athlete.query.all())
            })
        except:
            abort(422)  

        finally:
            db.session.close() 

    @app.route('/stats', methods=['POST'])
    def create_stat():
        body = request.get_json()

        athlete_id = body.get('athlete_id', None)
        avg_miles_per_week = body.get('avg_miles_per_week', None)
        avg_vertical_per_week = body.get('avg_vertical_per_week', None)
        longest_run = body.get('longest_run', None)
        longest_run_2_weeks = body.get('longest_run_2_weeks', None)
        race_distance = body.get('race_distance', None)
        race_veritcal = body.get('race_veritcal', None)
        race_date = body.get('race_date', None)

        if not ('athlete_id' in body):
            abort(404)

        try:
            stat = Stat(athlete_id=athlete_id, avg_miles_per_week=avg_miles_per_week, avg_vertical_per_week=avg_vertical_per_week, longest_run=longest_run, 
                longest_run_2_weeks=longest_run_2_weeks, race_distance=race_distance, race_veritcal=race_veritcal, race_date=race_date)
            db.session.add(stat)
            db.session.commit()

            return jsonify({
                'success': True,
                'created stat_id': stat.id,
                'total_stats': len(Stat.query.all())
            })
        except:
            abort(422)  

        finally:
            db.session.close()  

    @app.route('/stats/<int:stat_id>', methods=['DELETE'])
    def delete_stat(stat_id):
        try:
            stat = Stat.query.filter(Stat.id == stat_id).one_or_none()

            if stat is None:
                abort(404)

            db.session.delete(stat)
            db.session.commit()

            return jsonify({
                'success': True,
                'deleted_stat_id': stat_id,
                'total_stats_remaining': len(Stat.query.all())
            })

        except:
            abort(422)

        finally:
            db.session.close()
    
    
    @app.route('/')
    def hello_world():
        return "Hello, World!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()