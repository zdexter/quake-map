from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def db_add(obj, commit=True):
    db.session.add(obj)
    db.session.flush()
    if commit:
        db.session.commit()
    return obj

