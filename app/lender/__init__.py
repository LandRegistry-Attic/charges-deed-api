from flask import Blueprint
from . import server

blueprint = Blueprint('lender', __name__)
server.register_routes(blueprint)
