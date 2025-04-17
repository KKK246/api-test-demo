import requests
import unittest

class TestAuthAPI(unittest.TestCase):

    def test_successful_login(self):
        url = 'https://reqres.in/api/login'
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())
        print("✅ 成功登入，取得 token：", response.json()['token'])

    def test_login_missing_password(self):
        url = 'https://reqres.in/api/login'
        payload = {
            "email": "eve.holt@reqres.in"
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], "Missing password")
        print("❌ 登入失敗：缺少密碼")

    def test_login_wrong_credentials(self):
        url = 'https://reqres.in/api/login'
        payload = {
            "email": "wrong@email.com",
            "password": "wrongpassword"
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        print("❌ 登入失敗：帳號或密碼錯誤")
