from fe.models.core import asset as asset_model, \
        event as event_model, city as city_model
from fe.models import db_add
from fe import db
from geoalchemy2.elements import WKTElement

class EventDAL(object):

    @staticmethod
    def getNearbyCities(event):
        radius = 200000 # unit: meters
        distance_query = city_model.City.geog.ST_Distance(
            event.geog).label('distance')
        nearby_query = city_model.City.geog.ST_DWithin(
            event.geog,
            radius)
        city_query = db.session.query(city_model.City,
                distance_query)
        city_query = city_query.filter(nearby_query)
        cities = city_query.all()
        return cities

    @staticmethod
    def getAllQuakes():
        quake_query = event_model.Earthquake.query
        return quake_query.all()

    @staticmethod
    def createQuake(lat, lng, mag):
        event = event_model.Event()
        event.lat = lat
        event.lng = lng
        event.geog = WKTElement('POINT({} {})'.format(lng, lat)) # SRID 4326
        new_quake = event_model.Earthquake()
        new_quake.event = event
        new_quake.mag = mag
        return new_quake

    @staticmethod
    def addQuake(quake_to_add):
        return db_add(quake_to_add)

