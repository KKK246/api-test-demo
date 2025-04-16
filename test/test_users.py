import requests
import unittest

class TestUsersAPI(unittest.TestCase):
    def test_get_users(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

def test_sample_user():
    # 測試簡單數學運算是否正確
    assert 1 + 1 == 2

def test_user_name():
    # 假設有一個使用者名稱要驗證
    user_name = "edward"
    assert user_name.isalpha()  # 檢查是否只包含字母

def test_user_age_range():
    # 假設年齡不能小於 0 或大於 120
    age = 25
    assert 0 <= age <= 120
