from app.deed.model import Deed
import unittest
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.deed.helpers import DeedHelper


class TestDeedModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get(self):
        base_deed = DeedHelper._create_deed_db()
        deed = Deed.get(base_deed.id)

        self.assertEqual(deed.id, base_deed.id)

        DeedHelper._delete_deed(base_deed.id)

    @with_context
    def test_get_deed_by_token(self):
        base_deed = DeedHelper._create_deed_db()

        operative_deed_ = base_deed.json_doc['deed']["operative-deed"]
        base_deed_token = operative_deed_["borrowers"][0]["token"]

        retrieved_deed_from_token = Deed.get_deed_by_token(base_deed_token)

        self.assertEqual(base_deed.id,
                         retrieved_deed_from_token.id)
        self.assertEqual(base_deed.json_doc,
                         retrieved_deed_from_token.json_doc)

        DeedHelper._delete_deed(base_deed.id)

    @with_context
    def test_delete(self):
        base_deed = DeedHelper._create_deed_db()
        deed = Deed.get(base_deed.id)

        self.assertEqual(deed.id, DeedHelper._id)

        Deed.delete(deed.id)
        deed = Deed.get(deed.id)

        self.assertIs(deed, None)

    @with_context
    def test_borrower_has_signed(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        has_john_signed = Deed.borrower_has_signed(base_deed.id, johns_id)
        self.assertFalse(has_john_signed)

        base_deed.sign_deed(johns_id, 'I am John!')
        base_deed.save()

        has_john_signed = Deed.borrower_has_signed(base_deed.id, johns_id)
        self.assertTrue(has_john_signed)

    @with_context
    def test_all_borrowers_signed(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        has_john_signed = base_deed.all_borrowers_signed()
        self.assertFalse(has_john_signed)

        base_deed.sign_deed(johns_id, 'I am John!')
        base_deed.save()

        has_john_signed = base_deed.all_borrowers_signed()
        self.assertTrue(has_john_signed)

    @with_context
    def test_names_of_borrowers_signed_and_not(self):
        base_deed = DeedHelper._create_deed_db()
        johns_id = 1

        self.assertListEqual(
            ['John Smith'],
            Deed.names_of_all_borrowers_not_signed(base_deed.id)
        )
        self.assertListEqual(
            [],
            Deed.names_of_all_borrowers_signed(base_deed.id)
        )

        base_deed.sign_deed(johns_id, 'I am John!')
        base_deed.save()

        self.assertListEqual(
            [],
            Deed.names_of_all_borrowers_not_signed(base_deed.id)
        )
        self.assertListEqual(
            ['John Smith'],
            Deed.names_of_all_borrowers_signed(base_deed.id)
        )
