import unittest
import os
import requests
from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_is_main_routing_working(self):
        """
        Test if the main route is answering with the correct status code.
        """
        response = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(response.status_code, 200)

    def test_users(self):

        response = requests.get('http://127.0.0.1:5000/users')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
