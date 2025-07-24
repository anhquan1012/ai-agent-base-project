import json
import unittest
from fastapi.testclient import TestClient

from server import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hello_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.load(response), {"msg": "Hello world!"})
