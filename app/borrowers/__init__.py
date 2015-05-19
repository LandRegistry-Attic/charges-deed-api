from flask import Blueprint
from . import server

blueprint = Blueprint('borrowers', __name__)
server.register_routes(blueprint)
