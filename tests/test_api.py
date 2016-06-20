import unittest

from app import create_app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.flask_app = create_app()


    def test_basic_api_usage(self):
        self.assertIsNotNone(self.flask_app)

