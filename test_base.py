import unittest
import os
from flask_testing import TestCase
from app import app, db
from models import Risk, Field, create_risk


class MyTest(unittest.TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///risks.db"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):

        pass

    def test_risk(self):

        risk = Risk(name='AutoMobile')
        db.session.add(risk)
        db.session.commit()
        assert risk.name == 'AutoMobile'

    def test_field(self):

        field = Field(name='BMW', number='5544', date='2018-09-17')
        db.session.add(field)
        db.session.commit()
        assert field.name == 'BMW'


if __name__ == '__main__':
    unittest.main()
