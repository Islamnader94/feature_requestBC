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

    def test_add_route(self):

        response = requests.get('http://127.0.0.1:5000/add')
        self.assertEqual(response.status_code, 200)

    def test_addrisk_route(self):

        response = requests.get('http://127.0.0.1:5000/addrisk')
        self.assertEqual(response.status_code, 200)

    def test_review_route(self):

        response = requests.get('http://127.0.0.1:5000/review')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
