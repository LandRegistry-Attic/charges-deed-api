from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestGetConveyancer (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_conveyancer(self, client):
        response = client.get('/conveyancer')
        assert response.status_code == 200
        assert '"name": ""' in response.data.decode()
