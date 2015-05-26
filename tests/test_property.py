from tests.helpers import with_client, setUpApp, with_context
import unittest
import json


class TestGetProperty (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_lender(self, client):
        response = client.get('/property')
        assert response.status_code == 200
        data = json.loads(
            response.data.decode()).get('address').get('street-address')
        self.assertEquals(data, "Flat 16 Kingman Court")
