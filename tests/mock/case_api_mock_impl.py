from flask import jsonify
from flask.ext.api import status


class MockCaseApi(object):

    def update_status(self, deed_id, case_status):
        return jsonify(status_code=status.HTTP_200_OK)
