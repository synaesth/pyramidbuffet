from flask import Flask, session, g, render_template
from werkzeug.contrib.fixers import ProxyFix
from pyramidbuffet.database import connection
from flaskext.openid import OpenID


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('websiteconfig')
collection = connection['archive'].items

#from pyramidbuffet.openid_auth import DatabaseOpenIDStore
oid = OpenID(app, '/oid-store')
app.config['SECRET_KEY']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.before_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        g.user = User.query.filter_by(openid=openid).first()

@app.before_request
def get_stats():
    collection = connection['archive'].items
    g.text_count = collection.Item.find({'mediatype': 'texts'}).count()
    g.movie_count = collection.Item.find({'mediatype': 'movies'}).count()
    g.audio_count = collection.Item.find({'mediatype': 'audio'}).count()
    g.total_count = collection.Item.find().count()

from pyramidbuffet.views import general
from pyramidbuffet.views import details
app.register_blueprint(general.mod)
app.register_blueprint(details.mod)
