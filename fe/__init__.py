from flask import Flask
from flask.ext.assets import Environment
from flask.ext.sqlalchemy import SQLAlchemy
from models import db
from functools import partial

def __createDatabaseTables(app):
    from models.core import city, asset, event
    ctx = app.test_request_context()
    ctx.push()
    db.create_all()
    ctx.pop()

def createApp(config='fe.settings', debug=False):
    app = Flask(__name__)
    app.debug = debug
    if config:
        app.config.from_object(config)
    app.assets = Environment(app)

    db.init_app(app) # idempotently translate mapper classes to sql and create tables, relations etc accordingly

    __createDatabaseTables(app)

    return app

createDebugApp = partial(createApp, debug=True)
createProductionApp = partial(createApp)

#app = createProductionApp()
app = createDebugApp()

from fe import views

