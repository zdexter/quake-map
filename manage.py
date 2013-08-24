from flask.ext.script import Manager
from fe import createDebugApp

manager = Manager(createDebugApp)

@manager.command
def importCities():
    from fe.lib import parsers
    from fe.models.dal.city import CityDAL
    parser = parsers.GeonameParser()
    for city in parser.getCities():
        new_city = CityDAL.createCity(*city)
        CityDAL.addCity(new_city)

@manager.command
def importQuakes():
    from fe.models.dal.event import EventDAL
    from fe.lib import parsers
    parser = parsers.QuakeParser
    quakes = parser().quakes
    for quake in quakes:
        new_quake = EventDAL.createQuake(*quake)
        EventDAL.addQuake(new_quake)

if __name__ == '__main__':
    manager.run()

