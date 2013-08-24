quake-map
=========

A PostGIS2-backed {map,list} view of earthquakes from the last week, and cities that could be affected by those quakes or their aftershocks.

## Demo

Please visit the app on Heroku: [Quake Risk Map](http://quake-risk-map.herokuapp.com) (Currently disabled - no PostGIS on non-production tiers)

## Notes

### Performance Characteristics

More to come, but quickly:
	
- Bounding box construction is low-cost and the actual filter (ST_DWithin) is much faster than putting ST_Distance in the WHERE clause. ST_Distance actually solves the distance problem, whereas ST_DWithin just provides a boolean answer as to whether or not something is in the bounding box.
- Can increase speed by measuring distance on the sphere (not spheroid, which is what this currently uses) depending upon real-world accuracy and precision requirements.
	
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
