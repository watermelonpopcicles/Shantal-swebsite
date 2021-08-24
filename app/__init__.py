import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    pix = ["https://corgicare.com/wp-content/uploads/corgi-puppies.jpg", "https://handletheheat.com/wp-content/uploads/2021/06/homemade-vanilla-ice-cream.jpg", "https://i2.wp.com/smittenkitchen.com/wp-content/uploads/2021/06/chocolate-ice-cream-sandwiches-1-scaled.jpg?fit=1200%2C800&ssl=1", "https://img1.10bestmedia.com/Images/Photos/380699/GettyImages-855447930_54_990x660.jpg", "https://i.redd.it/zuzouqhc7ao41.jpg"]
    headline = ["Corgi", "Vanila Ice Cream", "Ice Cream Sandwitch", "Different Flavored Ice Cream", "Charcoal Ice Cream"]
    temp = getweather()
    return flask.render_template("index.html", icecreams = pix, title=headline, weather = temp)
def getweather ():
    city = "Lake Forest"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8fe79b85155beefc0a3882d4b1377ddd&units=imperial"
    x = requests.get(url)
    info=(x.content)
    info2=json.loads(info)
    temp = info2["main"]
    degrees = temp["temp"]
    return degrees

