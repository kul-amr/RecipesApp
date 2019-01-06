import os
import unittest
from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir


class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_dev(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']=='sqlite:///' + os.path.join(basedir, 'recipesapp.db'))

class TestTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_test(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']=='sqlite:///' + os.path.join(basedir, 'recipesapp_test.db'))


class TestProdConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_prod(self):
        self.assertTrue(app.config['DEBUG'] is False)



if __name__=='__main__':
    unittest.main()