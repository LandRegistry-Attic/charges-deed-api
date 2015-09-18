import json
from flask import jsonify, Response
from flask.ext.api import status
from .mock_response import MockResponse


class MockCaseApi(object):
    def update_status(self, deed_id, case_status):
        return jsonify(status_code=status.HTTP_200_OK)

    def get_borrowers(self, case_id):
        return MockResponse([{"last_name": "ggtg",
                "id": "25",
                "mobile_no": "09494309393",
                "type": "Borrower",
                "email_address": "a@b.com",
                "first_name": "rt",
                "middle_names": "",
                "address": ["2 rap street", "", "faketown", "F4K3"],
                "case_id": 16}])

    def get_property(self, case_id):
        return MockResponse({"title_number": "LO3827",
                            "id": 9,
                            "extended": "Market Square",
                            "street": "42A Broad Street",
                            "type": "Property",
                            "locality": "Slough",
                            "case_id": 19,
                            "tenure": "freehold",
                            "postcode": "SL2 1TP"})
