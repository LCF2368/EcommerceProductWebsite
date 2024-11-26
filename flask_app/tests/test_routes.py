import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestHomeRoute(unittest.TestCase):
    """Unit test class for testing the home route in a Flask application."""

    def setUp(self):
        """Set up a Flask test client."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        """Tear down resources after each test."""
        pass  # Add any cleanup code here if needed

    def test_home_route_invalid_method(self):
        """
        Test that the home route returns 405 when an invalid method is used.
        Purpose: Ensures the route has proper HTTP method handling.
        """
        response = self.client.post('/')  # Using POST instead of GET
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

if __name__ == "__main__":
    unittest.main()
