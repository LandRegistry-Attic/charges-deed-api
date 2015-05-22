from flask import Flask
from flask.ext.script import Manager
from app import helloworld


def create_manager():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)

    return manager
