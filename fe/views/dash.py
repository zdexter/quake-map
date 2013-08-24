from flask import render_template
from flask.json import jsonify
from fe import app
from fe.models.dal.event import EventDAL
from collections import defaultdict

@app.route('/')
def dashView(methods=['GET']):
    return render_template('dash.html')

@app.route('/quakes/list')
def quakeListView(methods=['GET']):
    # Just a way to trigger the query
    quakes = EventDAL.getAllQuakes()
    display_quakes = []
    # NOTE: In the real world this would be a REST endpoint called by JS
    # probably concurrently with page load and not in the render controller.
    # And it would stream data, not batch it like this
    for quake in quakes:
        nearby_cities = EventDAL.getNearbyCities(quake.event)
        display_quakes.append(((quake.event.lng, quake.event.lat),
                [(city.name, distance) for city, distance in nearby_cities]))
    return render_template('quake_list.html', quakes=display_quakes)

@app.route('/quakes/list_json')
def quakeListJsonView(methods=['GET']):
    quakes = EventDAL.getAllQuakes()
    display_quakes = defaultdict(str)
    # Same caveat as the above view
    for quake in quakes:
        nearby_cities = EventDAL.getNearbyCities(quake.event)
        quake_name = '{},{}'.format(quake.event.lng, quake.event.lat)
        display_quakes[quake_name] = [(city.name, distance) for city, distance in nearby_cities]
    return jsonify(quakes=display_quakes)

