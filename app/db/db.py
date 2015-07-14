from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()
migrate = Migrate(db)

json_type = JSON


def init(app, manager):
    db.init_app(app)
    migrate.init_app(app, db, 'app/db/migrations')
    manager.add_command('db', MigrateCommand)
