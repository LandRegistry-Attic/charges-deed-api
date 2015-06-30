import os

DEBUG = True

try:
    SQLALCHEMY_DATABASE_URI = os.getenv('DEED_DATABASE_URI','')
except KeyError:
    print("[ERROR] You need set the export variable for DEED_DATABASE_URI")
    raise