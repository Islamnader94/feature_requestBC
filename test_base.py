import unittest
import os
from flask_testing import TestCase
from app import app, db
from models import User, Client


class MyTest(unittest.TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///features.db"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):

        pass

    def test_user(self):

        user = User(first_name='Islam')
        db.session.add(user)
        db.session.commit()
        assert user.first_name == 'Islam'

    def test_client(self):

        client = Client(name='Client A')
        db.session.add(client)
        db.session.commit()
        assert client.name == 'Client A'


if __name__ == '__main__':
    unittest.main()
