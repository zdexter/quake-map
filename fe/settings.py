import os

PG_USER = os.environ['PG_USER']
PG_PASS = os.environ['PG_PASS']
PG_HOST = os.environ['PG_HOST']
PG_DB = os.environ['PG_DB']

SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}/{}'.format(
        PG_USER, PG_PASS, PG_HOST, PG_DB)

