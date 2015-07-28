from flask import Flask
from flask.ext.script import Manager
from app import helloworld, db
from app import deed, borrowers, conveyancer, property, lender
from app.service.case_api import make_case_client


def create_manager(case_api_client=make_case_client):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(deed.blueprint(case_api_client()))
    app.register_blueprint(borrowers.blueprint)
    app.register_blueprint(conveyancer.blueprint)
    app.register_blueprint(property.blueprint)
    app.register_blueprint(lender.blueprint)

    db.init(app, manager)

    return manager
