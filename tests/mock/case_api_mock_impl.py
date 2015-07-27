from flask import jsonify
from flask.ext.api import status


def update_status(deed_id, case_status):
    return jsonify(status_code=status.HTTP_200_OK)
