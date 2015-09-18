from flask import Response

class MockResponse(Response):
    def __init__(self, json_val):
        self.json_val = json_val

    def json(self):
        return self.json_val
