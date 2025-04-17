import requests
import unittest

class TestCreatePostAPI(unittest.TestCase):
    def test_create_post(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        data = {
            "title": "Test Post",
            "body": "This is a test post.",
            "userId": 1
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], data["title"])
