from flask import render_template
from fe import app
from fe.models.dal.event import EventDAL

@app.route('/')
def dashView(methods=['GET']):
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
    return render_template('dash.html', quakes=display_quakes)

