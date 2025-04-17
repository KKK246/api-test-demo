import requests
import unittest
import time
import concurrent.futures

class TestUsersAPI(unittest.TestCase):
    
    def test_get_users(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_users_response_time(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        self.assertLess(response_time, 1.0, "Response time is too high!")

    def test_invalid_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/invalid_endpoint'
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)

    def test_invalid_method(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.post(url)
        self.assertEqual(response.status_code, 405)

    def test_api_load(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        
        def fetch_data():
            response = requests.get(url)
            return response.status_code
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(fetch_data, range(10)))
        
        for status_code in results:
            self.assertEqual(status_code, 200)

    def test_user_data_integrity(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        users = response.json()
        
        for user in users:
            self.assertIn('name', user)
            self.assertIn('email', user)
            self.assertIn('address', user)
            self.assertTrue(user['name'])
            self.assertTrue(user['email'])
    
    def test_sql_injection(self):
        url = 'https://jsonplaceholder.typicode.com/users?name=1%27%20OR%201%3D1%20--'
        response = requests.get(url)
        self.assertNotIn('error', response.text)

