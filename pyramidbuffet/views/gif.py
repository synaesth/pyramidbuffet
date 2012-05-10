from flask import render_template
from pyramidbuffet import app
#import urllib2
#import simplejson as json


#______________________________________________________________________________
@app.route("/gif")
def details():
    return render_template('gif.html')
