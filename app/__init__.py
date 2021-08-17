import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    return "<p>hi everyone, I am making a website</p>"


