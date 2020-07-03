import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Actor, Movie, setup_db
from models import db


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.movie = {
            "title": "Movie Example",
            "release_date": "June 20, 2018"
        }

        self.actor = {
            "name": "Actor Example",
            "age": 20
            "gender": "Male"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actors_404(self):
        res = self.client().get('/actorsfail')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    def test_create_actors(self):
        res = self.client().post('/actors/create', json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_actors(self):
        res = self.client().patch('/actors/1', json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_actors_404(self):
        res.self.client().patch('/actors/1000', json=self.actor)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    def test_delete_actors(self):
        res = self.client().delete('/actors/1', json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_404(self):
        res = self.client().delete('/actors/1000', json=self.actor)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_get_movies_404(self):
        res = self.client().get('/moviesfail')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    def test_create_movies(self):
        res = self.client().post('/movies/create', json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_movies(self):
        res = self.client().patch('/movies/1', json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_movies_404(self):
        res = self.client().patch('/movies/1000', json=self.movie)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    def test_delete_movies(self):
        res = self.client().delete('/movies/1', json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_404(self):
        res = self.client().delete('/movies/1000', json=self.movie)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)


if __name__ == "__main__":
    unittest.main()
