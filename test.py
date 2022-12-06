import unittest

# Import the app module from app.py
from app import app

# Import Flask's test client
from flask.testing import FlaskClient

class TestApp(unittest.TestCase):
    # Set up a test client for the app
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the login route
    def test_login(self):
        # Test a successful login
        result = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Logged in successfully !', result.data)

        # Test a login with an incorrect password
        result = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'incorrect_password'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Incorrect username / password !', result.data)

    # Test the logout route
    def test_logout(self):
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)
        self.assertIn(b'You have been logged out', result.data)

    # Test the register route
    def test_register(self):
        # Test a successful registration
        result = self.app.post('/register', data={
            'email': 'test@example.com',
            'password': 'password',
            'confirm_password': 'password',
            'name': 'Test User',
            'cmp': 'Test Company',
            'in': '123456',
            'dl': 'DL123456',
            'age': '18',
            'pn': '1234567890',
            'gender': 'Male'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Account created successfully !', result.data)

        # Test a registration with a password and confirmation password that don't match
        result = self.app.post('/register', data={
            'email': 'test@example.com',
            'password': 'password',
            'confirm_password': 'incorrect_password',
            'name': 'Test User',
            'cmp': 'Test Company',
            'in': '123456',
            'dl': 'DL123456',
            'age': '18',
            'pn': '1234567890',
            'gender': 'Male'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Passwords do not match !', result.data)
