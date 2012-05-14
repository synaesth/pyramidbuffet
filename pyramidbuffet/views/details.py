from flask import Blueprint, render_template
from mongokit import Connection
from pyramidbuffet import database
from datetime import datetime

import urllib2
import simplejson as json

mod = Blueprint('details', __name__, url_prefix='/details')
connection = Connection()
connection.register(database.Item)
item = connection.Item()


#______________________________________________________________________________
@mod.route("/<identifier>")
def details(identifier):
    item_jstor = jstor(identifier)
    pyr_item = connection.Item.find_one({'identifier': identifier})
    if pyr_item:
        file_list = pyr_item['files']
        meta_dict = {k: v for k,v in item_dict(pyr_item).iteritems() if v != None}
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

## CREATE ITEM.
##______________________________________________________________________________
def create_item(json_str):
    if not json_str:
        return None
    metadata = json_str['metadata']
    identifier = metadata['identifier']
    pyr_metadata = item_dict(metadata)
    pyr_metadata['files'] = json_str['files']
    item_exists = connection.Item.find_one({'identifier': identifier})
    if item_exists:
        return None
    for k,v in pyr_metadata.iteritems():
        if k == 'date':
            item[k] = datetime.strptime(v, '%Y-%m-%d')
        elif k == 'files':
            item[k] = v
        elif k == 'subject':
            item[k] = v.split(';')
        else:
            item[k] = unicode(v)
    item.save()

# TESTING... 1 2 || 3 |4
#______________________________________________________________________________
def is_movie(mediatype):
    if mediatype == 'movies': return True

def is_audio(mediatype):
    if mediatype == 'audio': return True

def is_texts(mediatype):
    if mediatype == 'texts': return True
