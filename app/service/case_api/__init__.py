from . import implementation, interface


def make_case_client():
    return interface.CaseApiInterface(implementation)
