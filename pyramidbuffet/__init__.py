from flask import Flask, session, g, render_template
from flaskext.openid import OpenID

app = Flask(__name__)
app.config.from_object('websiteconfig')

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

from pyramidbuffet.views import general
from pyramidbuffet.views import details
app.register_blueprint(general.mod)
app.register_blueprint(details.mod)
