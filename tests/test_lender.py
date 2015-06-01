from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestGetLender (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_lender(self, client):
        response = client.get('/lender')
        assert response.status_code == 200
        assert '"name": "Bank of England Plc"' in response.data.decode()
