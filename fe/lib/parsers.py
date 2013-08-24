import requests, csv

# TODO: Error handling, real and robust parsers, etc.

class QuakeParser(object):
    """
    Parses USGS GeoJSON earthquake feeds.
    Usage:
        p = QuakeParser()
        p.quakes
    """
    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
    def __init__(self):
        r = requests.get(self.url)
        quakes_as_json = r.json()
        quakes_as_json = quakes_as_json['features']
        quakes = []
        for quake in quakes_as_json:
            mag = quake['properties']['mag']
            lat, lng = quake['geometry']['coordinates'][:2]
            quakes.append((lng, lat, mag))
        self.quakes = quakes

class GeonameParser(object):
    """
    Parses data in the format specified at this address:
    http://download.geonames.org/export/dump/readme.txt
    (tab-delimited, utf-8 encoded)
    """

    def __init__(self):
        f = open('fe/resources/cities.txt', 'r')
        self.reader = csv.reader(f, delimiter='\t')

    def getCities(self):
        for city in self.reader:
            yield city[1], city[4], city[5] # utf-8 name, lat, lng

