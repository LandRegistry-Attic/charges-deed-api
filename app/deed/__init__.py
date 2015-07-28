from flask import Blueprint
from . import server


def blueprint(case_api_client):
    blueprint = Blueprint('deed', __name__)
    server.register_routes(blueprint, case_api_client)
    return blueprint
