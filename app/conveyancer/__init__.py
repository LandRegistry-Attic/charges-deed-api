from flask import Blueprint
from . import server

blueprint = Blueprint('conveyancer', __name__)
server.register_routes(blueprint)
