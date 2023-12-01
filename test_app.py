import unittest
from app import app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_number(self):
        data = {"num1":2,"num2":3}
        response = self.app.post('/add', json=data)
        self.assertEqual(response.status_code, 200)
        result_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result_data['Addition'], 5)
if __name__=="__main__":
    unittest.main()