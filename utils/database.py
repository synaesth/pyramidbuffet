from flask import Flask
from mongokit import Connection, Document
import datetime

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create the little application object
app = Flask(__name__)
app.config.from_object(__name__)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
                                app.config['MONGODB_PORT'])



connection = Connection(MONGODB_HOST, MONGODB_PORT)

class Item(Document):
    __collection__ = 'items'
    __database__ = 'archive'
    structure = { }
    skip_validation = True
    use_autorefs = True
    default_values = { 'date': datetime.datetime.utcnow }
    use_dot_notation = True
connection.register(Item)    
