import os
from flask import Flask, request, abort, jsonify
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Actor, Movie, db_drop_and_create_all
from auth import AuthError, requires_auth


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__)
    CORS(app, resources={r"/api/": {"origins": "*"}})
    setup_db(app)

    db_drop_and_create_all()

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):

        actors = Actor.query.all()
        formatted_actors = [actor.model_format() for actor in actors]
        total_actors = len(actors)

        if total_actors == 0:
            abort(404)

        return jsonify({
            "success": True,
            "actors": formatted_actors,
            "total_actors": total_actors
        })

    @app.route('/actors/create', methods=['POST'])
    @requires_auth('create:actors')
    def create_actors(jwt):

        try:
            body = request.get_json()

            if not body:
                abort(400)

            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')

            actor = Actor(name=name, role=role, gender=gender)
            actor.insert()

            return jsonify({
                "success": True,
                "actor": actor.model_format()
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('edit:actors')
    def edit_actors(jwt, actor_id):

        try:
            current_actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if not current_actor:
                abort(404)

            body = request.get_json()

            if not body:
                abort(400)

            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')

            current_actor.name = name
            current_actor.age = age
            current_actor.gender = gender

            current_actor.update()

            return jsonify({
                "success": True,
                "actor": current_actor.model_format()
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actor_id):

        try:
            current_actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if not current_actor:
                abort(404)

            current_actor.delete()

            return jsonify({
                "success": True,
                "deleted_actor": actor_id
            })
        except Exception:
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):

        movies = Movie.query.all()
        formatted_movies = [movie.model_format() for movie in movies]
        total_movies = len(movies)

        if total_movies == 0:
            abort(404)

        return jsonify({
            "success": True,
            "movies": formatted_movies,
            "total_movies": total_movies
        })

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('create:movies')
    def create_movies(jwt):

        try:
            body = request.get_json()

            if not body:
                abort(400)

            title = body.get("title")
            release_date = body.get("release_date")

            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            return jsonify({
                "success": True,
                "movies": movie.model_format()
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('edit:movies')
    def edit_movies(jwt, movie_id):

        try:
            current_movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if not current_movie:
                abort(404)

            body = request.get_json()

            if not body:
                abort(400)

            title = body.get("title")
            release_date = body.get("release_date")

            current_movie.title = title
            current_movie.release_date = release_date

            current_movie.update()

            return jsonify({
                "success": True,
                "movie": current_movie.model_format()
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwt, movie_id):

        try:
            current_movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if not current_movie:
                abort(404)

            current_movie.delete()

            return jsonify({
                "success": True,
                "deleted_movie": movie_id
            })
        except Exception:
            abort(422)

    # --
    # Error Handlers
    # --

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error["description"]
        }), error.status_code

    # return app after all endpoints are created
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
