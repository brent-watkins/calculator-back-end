from django.test import TestCase
import json
import requests
from rest_framework import status

class OperationsTestCases(TestCase):
  json_headers = {"Accept": "application/json", "Content-Type": "application/json"}

  def setUp(self):
    requests.put("http://127.0.0.1:8000/api/register/", data=json.dumps({"balance": 6.00, "password": "Testing123", "status": "I", "username": "testing@testing.com"}), headers=self.json_headers)
    requests.put("http://127.0.0.1:8000/api/balance/", data=json.dumps({"balance": 6.00, "username": "testing@testing.com"}), headers=self.json_headers)

  def test_01_login(self):
    response = requests.post("http://127.0.0.1:8000/api/login/", data=json.dumps({"password": "Testing123", "username": "testing@testing.com"}), headers=self.json_headers)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_02_addition(self):
    no_operands = requests.post("http://127.0.0.1:8000/api/add/", data=json.dumps({"operands": [], "username": "testing@testing.com"}), headers=self.json_headers)
    one_operand = requests.post("http://127.0.0.1:8000/api/add/", data=json.dumps({"operands": ["5"], "username": "testing@testing.com"}), headers=self.json_headers)
    two_operands = requests.post("http://127.0.0.1:8000/api/add/", data=json.dumps({"operands": ["5", "10"], "username": "testing@testing.com"}), headers=self.json_headers)
    three_operands = requests.post("http://127.0.0.1:8000/api/add/", data=json.dumps({"operands": ["5", "10", "15"], "username": "testing@testing.com"}), headers=self.json_headers)
    invalid_operands = requests.post("http://127.0.0.1:8000/api/add/", data=json.dumps({"operands": ["A", "10"], "username": "testing@testing.com"}), headers=self.json_headers)

    self.assertEqual(no_operands.json(), 0)
    self.assertEqual(one_operand.json(), 5)
    self.assertEqual(two_operands.json(), 15)
    self.assertEqual(three_operands.json(), 30)
    self.assertEqual(invalid_operands.status_code, status.HTTP_400_BAD_REQUEST)

  def test_03_square_root(self):
    no_operand = requests.post("http://127.0.0.1:8000/api/square_root/", data=json.dumps({"operands": [], "username": "testing@testing.com"}), headers=self.json_headers)
    negative_operand = requests.post("http://127.0.0.1:8000/api/square_root/", data=json.dumps({"operands": ["-1"], "username": "testing@testing.com"}), headers=self.json_headers)
    invalid_operand = requests.post("http://127.0.0.1:8000/api/square_root/", data=json.dumps({"operands": ["A"], "username": "testing@testing.com"}), headers=self.json_headers)
    valid_operand = requests.post("http://127.0.0.1:8000/api/square_root/", data=json.dumps({"operands": ["100"], "username": "testing@testing.com"}), headers=self.json_headers)

    self.assertEqual(no_operand.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(negative_operand.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(invalid_operand.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(valid_operand.json(), 10)

  def test_04_no_balance(self):
    requests.put("http://127.0.0.1:8000/api/balance/", data=json.dumps({"balance": 1.00, "username": "testing@testing.com"}), headers=self.json_headers)
    balance_ok = requests.post("http://127.0.0.1:8000/api/multiply/", data=json.dumps({"operands": ["5", "10"], "username": "testing@testing.com"}), headers=self.json_headers)
    balance_empty = requests.post("http://127.0.0.1:8000/api/multiply/", data=json.dumps({"operands": ["5", "10"], "username": "testing@testing.com"}), headers=self.json_headers)
    
    self.assertEqual(balance_ok.json(), 50)
    self.assertEqual(balance_empty.status_code, status.HTTP_402_PAYMENT_REQUIRED)

