from flask.ext.assets import Bundle
from fe import app

js_libs = Bundle('js/libs/bootstrap.min.js', 'js/libs/angular.min.js',
        'js/libs/leaflet.js', 'js/libs/angular-leaflet-directive.min.js')
app.assets.register('js_libs', js_libs)

js_app = Bundle('js/app.js', 'js/controllers/dash.js')
app.assets.register('js_app', js_app)

css_libs = Bundle('css/libs/bootstrap.min.css', 'css/libs/leaflet.css')
app.assets.register('css_libs', css_libs)

css_app = Bundle('css/app.css')
app.assets.register('css_app', css_app)

