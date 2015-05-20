from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestGetProperty (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_lender(self, client):
        response = client.get('/get-property')
        assert response.status_code == 200
        assert '"property_addr_1": "Flat 16 Kingman Court",' in response.data.decode()
