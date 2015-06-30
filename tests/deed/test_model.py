from app.deed.model import Deed
import unittest
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.deed.helpers import DeedHelper


class TestCaseModel (unittest.TestCase):

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

    # @with_context
    # def test_get(self):
    #     case_id = CaseHelper._create_case_db()
    #     case = Case.get(case_id)
    #
    #     self.assertEqual(case.id, case_id)
    #
    #     CaseHelper._delete_case(case_id)
    #
    # @with_context
    # def test_delete(self):
    #     case_id = CaseHelper._create_case_db()
    #     case = Case.get(case_id)
    #
    #     self.assertEqual(case.id, CaseHelper._id)
    #
    #     Case.delete(case.id)
    #     case = Case.get(case.id)
    #
    #     self.assertIs(case, None)
    #
    # @with_context
    # def test_to_json(self):
    #     case = CaseHelper._create_case()
    #
    #     case_as_json = case.to_json()
    #
    #     self.assertEqual(case_as_json["id"], CaseHelper._id)
    #     self.assertEqual(case_as_json["deed_id"], CaseHelper._deed_id)
    #     self.assertEqual(case_as_json["conveyancer_id"], CaseHelper._conveyancer_id)
    #     self.assertEqual(case_as_json["status"], CaseHelper._status)
    #     self.assertEqual(case_as_json["last_updated"], serialize_datetime(
    #         CaseHelper._last_updated.isoformat()))
    #     self.assertEqual(case_as_json["created_on"], serialize_datetime(
    #         CaseHelper._created_on.isoformat()))
    #
    # @with_context
    # def test_from_json(self):
    #
    #     case = CaseHelper._create_case()
    #
    #     self.assertEqual(case.id, CaseHelper._id)
    #     self.assertEqual(case.deed_id, CaseHelper._deed_id)
    #     self.assertEqual(case.conveyancer_id, CaseHelper._conveyancer_id)
    #     self.assertEqual(case.status, CaseHelper._status)
    #     self.assertEqual(case.last_updated, CaseHelper._last_updated)
    #     self.assertEqual(case.created_on, CaseHelper._created_on)
    #
    # @with_context
    # def test_model(self):
    #     case = CaseHelper._create_case()
    #
    #     self.assertEqual(case.id, CaseHelper._id)
    #     self.assertEqual(case.deed_id, CaseHelper._deed_id)
    #     self.assertEqual(case.conveyancer_id, CaseHelper._conveyancer_id)
    #     self.assertEqual(case.status, CaseHelper._status)
    #     self.assertEqual(case.last_updated, CaseHelper._last_updated)
    #     self.assertEqual(case.created_on, CaseHelper._created_on)
