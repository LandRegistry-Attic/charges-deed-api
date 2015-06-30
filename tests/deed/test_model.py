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
    def test_get_all(self):
        deed_id = DeedHelper._create_deed_db()
        deed = Deed.get(deed_id)

        self.assertIn(deed, Deed.all())

        DeedHelper._delete_deed(deed_id)

        self.assertNotIn(deed, Deed.all())

    @with_context
    def test_get(self):
        deed_id = DeedHelper._create_deed_db()
        deed = Deed.get(deed_id)

        self.assertEqual(deed.id, deed_id)

        DeedHelper._delete_deed(deed_id)

    @with_context
    def test_delete(self):
        deed_id = DeedHelper._create_deed_db()
        deed = Deed.get(deed_id)

        self.assertEqual(deed.id, DeedHelper._id)

        Deed.delete(deed.id)
        deed = Deed.get(deed.id)

        self.assertIs(deed, None)
