# flake8:noqa
from app.db.db import *
from app.db import init

class AlembicVersion(db.Model):
    __tablename__ = 'alembic_version'

    version_num = db.Column(db.String(), primary_key=True)
