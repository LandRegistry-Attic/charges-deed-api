from tests.helpers import with_client, setUpApp, with_context
import json
import unittest


class TestViewDeed (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_deed(self, client):
        response = client.get('/deed/1')
        self.assertEquals(response.status_code, 200)
        json_response = json.loads(response.data.decode())
        self.assertEquals("1", json_response["id"])
