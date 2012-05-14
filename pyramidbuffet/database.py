from mongokit import Document
import datetime

class Item(Document):
    __collection__ = 'items'
    __database__ = 'archive'
    structure = {
        'identifier': unicode,
        'title': unicode,
        'description': unicode,
        'mediatype': unicode,
        'creator': unicode,
        'date': datetime.datetime,
        'contact': unicode,
        'credits': unicode,
        'subject': list,
        'notes': unicode,
        'coverage': unicode,
        'licenseurl': unicode,
        'rights': unicode,
        'contributor': unicode,
        'publisher': unicode,
        'credits': unicode,
        'language': unicode,
        'files': list,
    }
    required_fields = ['title']
    default_values = {
        'date': datetime.datetime.utcnow
    }
