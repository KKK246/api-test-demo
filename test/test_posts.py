import requests
import unittest

class TestPostsAPI(unittest.TestCase):
    def test_get_posts(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

