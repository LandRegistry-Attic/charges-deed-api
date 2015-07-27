class CaseApiInterface(object):
    def __init__(self, implementation):
        self.implementation = implementation

    def update_status(self, deed_id, status):
        return self.implementation.update_status(deed_id, status)
