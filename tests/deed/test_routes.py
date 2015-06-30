import unittest
from random import randint

from flask.ext.api import status
from app.deed.model import Deed
from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.deed.helpers import DeedHelper


class TestDeedRoutes(unittest.TestCase):
    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_route(self, client):
        deed_id = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(str(deed_id) in response.data.decode())

        DeedHelper._delete_deed(deed_id)

    @with_context
    @with_client
    def test_no_get_route(self, client):
        response = client.get('/deed/{}'.format(randint(1, 9999999)))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @with_context
    @with_client
    def test_delete_route(self, client):
        deed_id = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        Deed.delete(deed_id)

        response = client.get('/deed/{}'.format(deed_id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
