from flask.ext.script import Manager
from flask.ext.api import FlaskAPI
from app import helloworld, db
from app import deed
from app.service.case_api import CaseApi


def create_manager(case_api_client=CaseApi):
    app = FlaskAPI(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(deed.blueprint(case_api_client()))

    db.init(app, manager)

    return manager
