from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestViewDeed (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_deed(self, client):
        response = client.get('/deed/1')
        assert response.status_code == 200
        assert '"deed-id": "12345"' in response.data.decode()
