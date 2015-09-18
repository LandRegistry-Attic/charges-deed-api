import json
from flask import jsonify, Response
from flask.ext.api import status


class MockCaseApi(object):

    def update_status(self, deed_id, case_status):
        return jsonify(status_code=status.HTTP_200_OK)

    def get_borrowers(self, case_id):
        borrower_json =[{"last_name": "ggtg",
                "id": "25",
                "mobile_no": "09494309393",
                "type": "Borrower",
                "email_address": "a@b.com",
                "first_name": "rt",
                "middle_names": "",
                "address": ["2 rap street", "", "faketown", "F4K3"],
                "case_id": 16}]

        return Response(borrower_json, status=200, mimetype="application/json")

    def get_property(self, case_id):

        return {"title": {
            "address": {
                "street-address": "test street",
                "postal-code": "RG1 1DP",
                "locality": "London",
                "extended-address": "test-extended address"
            },
            "title-number": "123ABC"
        }}
