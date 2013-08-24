quake-map
=========

A PostGIS2-backed {map,list} view of earthquakes from the last week, and cities that could be affected by those quakes or their aftershocks.

## Demo

Please visit the app on Heroku: [Quake Risk Map](http://quake-risk-map.herokuapp.com)
	
## Notes

### Performance Characteristics

More to come, but quickly:
	- Bounding box construction is low-cost and the actual filter (ST_DWithin) is much faster than
		putting distance in the WHERE clause.
	- Can increase speed by measuring distance on the sphere (not spheroid, which is what this currently uses) depending upon real-world accuracy and precision requirements
	
## Hacking

### Installation

Clone the repository. Then:

	virtualenv --distribute venv && source venv/bin/activate
	pip install -r requirements.txt
	touch .env # Now, edit and add local Postgres credentials - see fe/settings.py
	foreman start

### Deployment

	heroku create
	git push heroku master
