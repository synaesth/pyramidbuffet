from flask import Flask
from mongokit import Connection, Document
from pyramidbuffet import app
import datetime

#app = Flask(__name__)
#app.config.from_object(__name__)
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])

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
connection.register(Item)
