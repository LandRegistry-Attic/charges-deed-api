from flask import Blueprint
from . import server

blueprint = Blueprint('deed', __name__)
server.register_routes(blueprint)
