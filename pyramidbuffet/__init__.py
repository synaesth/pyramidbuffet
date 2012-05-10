from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from pyramidbuffet.views import details
from pyramidbuffet.views import gif
#from views import details
