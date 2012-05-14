from flask import Flask
from mongokit import Connection, Document
import datetime

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
connection = Connection(MONGODB_HOST, MONGODB_PORT)

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
