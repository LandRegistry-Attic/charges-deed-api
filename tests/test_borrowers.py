from tests.helpers import with_client, setUpApp, with_context
import unittest
from lxml.html import document_fromstring


class TestGetBorrower (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_borrower(self, client):
        response = client.get('/get-borrower/1')
        assert response.status_code == 200
        assert '"borrower_forename": "Peter"' in response.data.decode()
