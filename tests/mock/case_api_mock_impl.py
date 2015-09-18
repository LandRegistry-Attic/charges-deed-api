from flask import jsonify
from flask.ext.api import status
from .mock_response import MockResponse


class MockCaseApi(object):
    def update_status(self, deed_id, case_status):
        return jsonify(status_code=status.HTTP_200_OK)

    def get_borrowers(self, case_id):
        return MockResponse([
            {
                "id": "1",
                "name": "John Smith",
                "address": {
                    "street-address": "test street",
                    "postal-code": "RG1 1DP",
                    "locality": "London",
                    "extended-address": "test-extended address"
                }
            }
        ])

    def get_property(self, case_id):
        return MockResponse({"title_number": {
            "address": {
                "street-address": "test street",
                "postal-code": "RG1 1DP",
                "locality": "London",
                "extended-address": "test-extended address"
            },
            "title-number": "123ABC"
        }})
