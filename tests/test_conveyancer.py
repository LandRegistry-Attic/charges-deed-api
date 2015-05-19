from tests.helpers import with_client, setUpApp, with_context
import unittest
from lxml.html import document_fromstring


class TestGetConveyancer (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_conveyancer(self, client):
        response = client.get('/get-conveyancer')
        assert response.status_code == 200
        assert '"conveyancer_name": ""' in response.data.decode()
