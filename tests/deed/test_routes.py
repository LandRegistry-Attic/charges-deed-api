import unittest
from random import randint

from flask.ext.api import status
from flask import json
from app.deed import service as deed_service
from tests.helpers import with_client, setUpApp, \
    with_context, setUpDB, tearDownDB
from tests.deed.helpers import DeedHelper
from tests.mock.case_api_mock_impl import MockCaseApi


class TestDeedRoutes(unittest.TestCase):
    def setUp(self):
        setUpApp(self, case_api_client=MockCaseApi)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_route(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(str(deed.id) in response.data.decode())

        DeedHelper._delete_deed(deed.id)

    @with_context
    @with_client
    def test_no_get_route(self, client):
        response = client.get('/deed/{}'.format(randint(1, 9999999)))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @with_context
    @with_client
    def test_delete_route(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        deed_service.delete(deed.id)

        response = client.get('/deed/{}'.format(deed.id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @with_context
    @with_client
    def test_sign_route(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        signature = "@#$%%^&"
        payload = json.dumps({
            "signature": signature
        })
        response = client.post(
            '/deed/{}/{}/signature/'.format(deed.id, "1"),
            data=payload,
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(str(signature) in response.data.decode())

        DeedHelper._delete_deed(deed.id)

    @with_context
    @with_client
    def test_sign_route_forbidden(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}'.format(deed.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        signature = "@#$%%^&"
        response = client.post('/deed/{}/{}/signature/'
                               .format(deed.id, "10"),
                               data={"signature": signature})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        DeedHelper._delete_deed(deed.id)

    @with_context
    @with_client
    def test_create_generates_token(self, client):
        headers = {'content-type': 'application/json'}
        response = client.post('/deed/', data=json.dumps(DeedHelper._json_doc),
                               headers=headers)

        result = json.loads(response.data.decode())
        get_response = client.get('/deed/{}'.format(result['id']))

        self.assertTrue("token" in get_response.data.decode())

        DeedHelper._delete_deed(result['id'])

    @with_context
    @with_client
    def test_get_by_token(self, client):
        deed = DeedHelper._create_deed_db()

        deed_json = deed.json_doc['deed']
        token = deed_json["operative-deed"]["borrowers"][0]["token"]
        response = client.get('/deed/borrower/{}'.format(token))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(str(token) in response.data.decode())

        DeedHelper._delete_deed(deed.id)

    @with_context
    @with_client
    def test_confirm_completion(self, client):
        deed = DeedHelper._create_deed_db()

        signature = 'SIGNATURE'
        registrars_signature = {
            "registrars-signature": signature
        }
        response = client.post('/deed/{}/completion'.format(deed.id),
                               data=registrars_signature)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        get_response = client.get('/deed/{}'.format(deed.id))

        deed_json = get_response.data.decode()
        self.assertIn('"registrars-signature": "{}"'.format(signature),
                      deed_json)

        DeedHelper._delete_deed(deed.id)

    @with_context
    @with_client
    def test_confirm_completion_deed_not_found(self, client):
        signature = 'SIGNATURE'
        registrars_signature = {
            "registrars-signature": signature
        }
        response = client.post('/deed/{}/completion'.format(1234),
                               data=registrars_signature)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @with_context
    @with_client
    def test_get_names_signed(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}/signed/name'.format(deed.id))
        resp_json = json.loads(response.data)

        self.assertEquals([], resp_json['names'])

        deed_service.sign_deed(deed, 1, "I'm John Smith!")
        deed.save()

        response = client.get('/deed/{}/signed/name'.format(deed.id))
        resp_json = json.loads(response.data)

        self.assertEquals(['John Smith'], resp_json['names'])

    @with_context
    @with_client
    def test_get__signed_status(self, client):
        deed = DeedHelper._create_deed_db()

        response = client.get('/deed/{}/signed_status'.format(deed.id))
        resp_json = json.loads(response.data)

        self.assertEquals(['John Smith'], resp_json['names'])
        self.assertFalse(resp_json['all_signed'])

        deed_service.sign_deed(deed, 1, "I'm John Smith!")
        deed.save()

        response = client.get('/deed/{}/signed_status'.format(deed.id))
        resp_json = json.loads(response.data)

        self.assertEquals([], resp_json['names'])
        self.assertTrue(resp_json['all_signed'])
