from flask import render_template
from pyramidbuffet import app
import urllib2
import simplejson as json


#______________________________________________________________________________
@app.route("/")
def index():
    return render_template('index.html')

#______________________________________________________________________________
@app.route("/details/<identifier>")
def details(identifier):
    item_jstor = jstor(identifier)
    meta_dict = item_jstor['metadata']
    env.tests['movies'] = movies
    return render_template('details.html', files=item_jstor['files'],
                                           item=meta_dict)
# Item JSON store.
#______________________________________________________________________________
def jstor(identifier):
    url = 'http://archive.org/metadata/%s' % identifier
    return json.loads(urllib2.urlopen(url).read())
