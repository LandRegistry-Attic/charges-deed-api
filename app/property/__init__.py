from flask import Blueprint
from . import server

blueprint = Blueprint('property', __name__)
server.register_routes(blueprint)
