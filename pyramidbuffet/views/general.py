from flask import Blueprint, render_template, g, request
from pyramidbuffet import oid
from pyramidbuffet.database import connection

mod = Blueprint('general', __name__)
collection = connection['archive'].items


# PYRAMID BUFFET HOME PAGE
#______________________________________________________________________________
@mod.route("/")
def index():
    pyr_items = [ x for x in collection.Item.find() ]
    return render_template('index.html', pyr_items=pyr_items)

# <<__ LOGIN __>>> LOG OUT <<
#______________________________________________________________________________
@mod.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.form.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['email', 'fullname',
                                                  'nickname'])
    return render_template('login.html', next=oid.get_next_url(),
                           error=oid.fetch_error())
@mod.route("/logout")
def logout():
    session.pop('openid', None)
    flash(u'You were signed out')
    return redirect(oid.get_next_url())
