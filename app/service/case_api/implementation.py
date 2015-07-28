import requests

from app import config

CASE_API_BASE_HOST = config.CASE_API_BASE_HOST


def update_status(deed_id, status):
    body = {"status": status}
    url = CASE_API_BASE_HOST + "/case/" + str(deed_id) + "/status"
    return requests.post(url, data=body)
