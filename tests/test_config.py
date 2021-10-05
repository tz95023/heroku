# tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'], 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'], 'postgresql://postgres:953515@localhost:5433/da-flask-app'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'], 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'], 'postgresql://postgres:953515@localhost:5433/da-flask-app_test'
        )
