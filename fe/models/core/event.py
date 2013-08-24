from fe import db
from sqlalchemy.ext.hybrid import hybrid_property
from geoalchemy2.types import Geography
import datetime

class Event(db.Model):
    id =            db.Column(db.Integer, db.Sequence('event_seq_id'), primary_key=True)
    lat =           db.Column(db.Float)
    lng =           db.Column(db.Float)
    geog =          db.Column(Geography(geometry_type='POINT', srid=4326))
    _created =      db.Column('created', db.DateTime, nullable=False, default=
            datetime.datetime.now)

    @hybrid_property
    def created(self):
        return self._created.strftime('%a %b %d %Y %I:%M %p')

class Earthquake(db.Model):
    id =            db.Column(db.Integer, db.Sequence('earthquake_seq_id'), primary_key=True)
    # TODO: Cascade quake -> event (if that's desirable - depends on use case really)
    event_id =      db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), primary_key=True)
    event =         db.relationship('Event', primaryjoin='Earthquake.event_id==Event.id', uselist=False)
    mag =           db.Column(db.Numeric(precision=3, scale=2)) # 3 total numbers and 2 after radix

