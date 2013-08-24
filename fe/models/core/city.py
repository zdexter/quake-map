from fe import db
from geoalchemy2.types import Geography

class City(db.Model):
    id =            db.Column(db.Integer, db.Sequence('city_seq_id'), primary_key=True)
    name =          db.Column(db.Unicode(255))
    latitude =      db.Column(db.Float)
    longitude =     db.Column(db.Float)
    geog =          db.Column(Geography(geometry_type='POINT', srid=4326))

