import requests
from app import config


class CaseApi(object):
    CASE_API_BASE_HOST = config.CASE_API_BASE_HOST

    def update_status(self, deed_id, status):
        body = {"status": status}
        url = "{base}/case/{deed_id}/status".format(
            base=self.CASE_API_BASE_HOST,
            deed_id=str(deed_id)
        )
        return requests.post(url, data=body)

    def get_borrowers(self, case_id):
        url = "{base}/case/{case_id}/borrowers"
        return requests.get(url)
            
