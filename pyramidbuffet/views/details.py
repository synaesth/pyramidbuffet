from flask import Blueprint, render_template
import urllib2
import simplejson as json

mod = Blueprint('details', __name__, url_prefix='/details')


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
