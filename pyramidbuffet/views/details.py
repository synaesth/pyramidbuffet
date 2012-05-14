from flask import Blueprint, render_template
from pyramidbuffet.database import connection

import urllib2
import simplejson as json

mod = Blueprint('details', __name__, url_prefix='/details')
collection = connection['archive'].items


#______________________________________________________________________________
@mod.route("/<identifier>")
def details(identifier):
    item_jstor = jstor(identifier)
    #pyr_item = connection.Item.find_one({'identifier': identifier})
    pyr_item = collection.Item.find_one({'identifier': identifier})
    if pyr_item:
        file_list = pyr_item['files']
        meta_dict = {k: v for k,v in item_dict(pyr_item).iteritems() if v != None}
        subject = meta_dict['subject'].split(';')
        meta_dict['subject'] = subject
        return render_template('details.html', files=file_list,
                                               metadata=meta_dict)
    return render_template('404.html'), 404

# Item JSON store.
#______________________________________________________________________________
def jstor(identifier):
    url = 'http://archive.org/metadata/%s' % identifier
    return json.loads(urllib2.urlopen(url).read())

# IA Meta-dict => PYRBUF Meta-dict
#______________________________________________________________________________
def item_dict(item_jstor):
    pyr_meta = ['identifier', 'title', 'description', 'mediatype', 'creator',
                'date', 'contact', 'credits', 'subject', 'notes', 'coverage',
                'licenseurl', 'rights', 'contributor', 'publisher', 'credits',
                'language']
    return {k: v for k,v in item_jstor.iteritems() if k in pyr_meta}
