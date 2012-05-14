#!/usr/bin/env python

from mongokit import Connection
from database import Item
from database import connection
from datetime import datetime
import sys

import urllib2
import simplejson as json

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

def get_date(date_str):
    try:  
        return datetime.strptime(date_str, '%Y-%m-%d')
    except:
        pass
    try:  
        return datetime.strptime(date_str, '%Y')
    except:
        pass
    try:  
        return datetime.strptime(date_str, '%Y-%m')
    except:
        pass
    try:  
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except:
        pass
    return None    
    

## CREATE ITEM.
##______________________________________________________________________________
def createitem(json_str):
    collection = connection['archive'].items
    item = collection.Item()
    if not json_str['metadata']:
        return None
    metadata = json_str['metadata']
    identifier = metadata['identifier']
    pyr_metadata = item_dict(metadata)
    pyr_metadata['files'] = json_str['files']
    item_exists = connection.Item.find_one({'identifier': identifier})
    if item_exists:
        #print 'SKIPPING :: "%s" is already in the buffet!' % identifier
        return None
    for k,v in pyr_metadata.iteritems():
        if k == 'date':
            date = get_date(v)
            if not date:
                date = get_date(metadata['publicdate'])
            item[k] = date
        elif k == 'files':
            item[k] = v
        elif k == 'subject':
            item[k] = v
        else:
            item[k] = v
    item.save()
    print 'SUCCESS :: "%s" added to the buffet' % identifier

for i in open(sys.argv[1]):
    createitem(jstor(i))
