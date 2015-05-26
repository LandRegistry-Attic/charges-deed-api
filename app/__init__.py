from flask import Flask
from flask.ext.script import Manager
from app import helloworld
from app import deed, borrowers, conveyancer, property, lender


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(deed.blueprint)
    app.register_blueprint(borrowers.blueprint)
    app.register_blueprint(conveyancer.blueprint)
    app.register_blueprint(property.blueprint)
    app.register_blueprint(lender.blueprint)

    return app, manager
