quake-map
=========

A PostGIS2-backed {map,list} view of earthquakes from the last week, and cities that could be affected by those quakes or their aftershocks.

## Demo

Please visit the app on Heroku: [Quake Risk Map](http://quake-risk-map.herokuapp.com) (Currently disabled - no PostGIS on non-production tiers)

## Notes

### Performance Characteristics

Please see this repository's [detailed wiki article](https://github.com/zdexter/quake-map/wiki/Efficiently-finding-cities-near-earthquake-events) on efficiently finding cities near earthquakes events.
	
## Hacking

### Installation

Clone the repository. Then:

	virtualenv --distribute venv && source venv/bin/activate
	pip install -r requirements.txt
	touch .env # Now, edit and add local Postgres credentials - see fe/settings.py

### Running: Development

	foreman start

### Grabbing USGS and city data

To import a large list of cities and their geographic coordinates:

	python manage.py importCities

To import all of the earthquakes from the past week from the USGS GeoJSON API:

	python manage.py importQuakes
	
### Running: Production

	heroku create
	git push heroku master
	heroku addons:add heroku-postgresql:dev
	heroku pg:psql	# Opens a psql prompt

In the psql prompt:

	CREATE EXTENSION postgis;
