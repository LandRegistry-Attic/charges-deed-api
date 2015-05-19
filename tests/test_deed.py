from tests.helpers import with_client, setUpApp, with_context
import unittest
from lxml.html import document_fromstring


class TestViewDeed (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_deed(self, client):
        response = client.get('/view-deed')
        assert response.status_code == 200
        assert '"deed_id": "123456"' in response.data.decode()
