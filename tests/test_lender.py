from tests.helpers import with_client, setUpApp, with_context
import unittest
from lxml.html import document_fromstring


class TestGetLender (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_lender(self, client):
        response = client.get('/get-lender')
        assert response.status_code == 200
        assert '"lender_name": "Bank of England Plc"' in response.data.decode()
