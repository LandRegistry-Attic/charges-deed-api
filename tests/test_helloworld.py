from tests.helpers import with_client, setUpApp, with_context
from flask import json
import unittest


class TestHelloWorld (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_api(self, client):
        response = client.get('/helloworld')
        assert response.status_code == 200

        result = json.loads(response.data.decode())
        assert '"Hello": "World"' in result
