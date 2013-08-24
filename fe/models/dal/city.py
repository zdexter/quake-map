from fe.models.core import city as city_model
from fe.models import db_add
from geoalchemy2.elements import WKTElement

class CityDAL(object):

    @staticmethod
    def createCity(name, lat, lng):
        new_city = city_model.City()
        new_city.name = name
        new_city.lat = lat
        new_city.lng = lng
        new_city.geog = WKTElement('POINT({} {})'.format(lng, lat))
        return new_city

    @staticmethod
    def addCity(city_to_add):
        return db_add(city_to_add)

