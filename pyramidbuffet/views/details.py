from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader

import urllib2
import simplejson as json

mod = Blueprint('details', __name__, url_prefix='/details')
env = Environment()


#______________________________________________________________________________
@mod.route("/<identifier>")

def details(identifier):
    item_jstor = jstor(identifier)
    meta_dict = item_jstor['metadata']
    return render_template('details.html', files=item_jstor['files'],
                                           item=meta_dict)
# Item JSON store.
#______________________________________________________________________________
def jstor(identifier):
    url = 'http://archive.org/metadata/%s' % identifier
    return json.loads(urllib2.urlopen(url).read())

def is_movie(mediatype):
    if mediatype == 'movies': return True

def is_audio(mediatype):
    if mediatype == 'audio': return True

def is_texts(mediatype):
    if mediatype == 'texts': return True

env.tests['movies'] = is_movie
env.tests['audio'] = is_audio
env.tests['texts'] = is_texts
