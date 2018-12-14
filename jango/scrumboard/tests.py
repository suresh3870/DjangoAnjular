from django.test import TestCase

from rest_framework.test import RequestsClient


class ApiTest(TestCase):
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/admin/')
    assert response.status_code == 200
