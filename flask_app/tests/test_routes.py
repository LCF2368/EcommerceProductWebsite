import unittest
from flask_app.app import app

class TestRoutes(unittest.TestCase):
    # Set up the Flask test client before each test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test 1: Check if the home route returns a 200 status code
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected text (adjust as needed)
        self.assertIn(b'Welcome', response.data)

    # Test 2: Check if the /products route returns a 200 status code
    def test_products_route(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected text (adjust as needed)
        self.assertIn(b'Products', response.data)

    # Test 3: Check if a POST request to the / route returns a 405 status code (Method Not Allowed)
    def test_home_route_post(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)  # 405 means method not allowed

if __name__ == '__main__':
    unittest.main()
