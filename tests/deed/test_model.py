from app.deed import service as deed_service
import unittest
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.deed.helpers import DeedHelper
from tests.mock.case_api_mock_impl import MockCaseApi


class TestDeedModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self, case_api_client=MockCaseApi)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get(self):
        base_deed = DeedHelper._create_deed_db()
        deed = deed_service.get(base_deed.id)

        self.assertEqual(deed.id, base_deed.id)

        DeedHelper._delete_deed(base_deed.id)

    @with_context
    def test_get_deed_by_token(self):
        base_deed = DeedHelper._create_deed_db()

        operative_deed_ = base_deed.json_doc['deed']["operative-deed"]
        base_deed_token = operative_deed_["borrowers"][0]["token"]

        retrieved_deed_from_token = deed_service.get_deed_by_token(
            base_deed_token
        )

        self.assertEqual(base_deed.id,
                         retrieved_deed_from_token.id)
        self.assertEqual(base_deed.json_doc,
                         retrieved_deed_from_token.json_doc)

        DeedHelper._delete_deed(base_deed.id)

    @with_context
    def test_delete(self):
        base_deed = DeedHelper._create_deed_db()
        deed = deed_service.get(base_deed.id)

        self.assertEqual(deed.id, DeedHelper._id)

        deed_service.delete(deed.id)
        deed = deed_service.get(deed.id)

        self.assertIs(deed, None)

    @with_context
    def test_borrower_has_signed(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        has_john_signed = deed_service.borrower_has_signed(base_deed.id,
                                                           johns_id)
        self.assertFalse(has_john_signed)

        deed_service.sign_deed(base_deed, johns_id, 'I am John!')
        base_deed.save()

        has_john_signed = deed_service.borrower_has_signed(base_deed.id,
                                                           johns_id)
        self.assertTrue(has_john_signed)

    @with_context
    def test_all_borrowers_signed(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        has_john_signed = deed_service.all_borrowers_signed(base_deed)
        self.assertFalse(has_john_signed)

        deed_service.sign_deed(base_deed, johns_id, 'I am John!')
        base_deed.save()

        has_john_signed = deed_service.all_borrowers_signed(base_deed)
        self.assertTrue(has_john_signed)

    @with_context
    def test_names_of_borrowers_signed_and_not(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        self.assertListEqual(
            ['John Smith'],
            deed_service.names_of_all_borrowers_not_signed(base_deed.id)
        )
        self.assertListEqual(
            [],
            deed_service.names_of_all_borrowers_signed(base_deed.id)
        )

        deed_service.sign_deed(base_deed, johns_id, 'I am John!')
        base_deed.save()

        self.assertListEqual(
            [],
            deed_service.names_of_all_borrowers_not_signed(base_deed.id)
        )
        self.assertListEqual(
            ['John Smith'],
            deed_service.names_of_all_borrowers_signed(base_deed.id)
        )
