from flask import Flask,render_template,request
from geopy.geocoders import Nominatim
from geopy import distance

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":

        geocoder = Nominatim(user_agent="Distance Calculator")

        location1 = request.form.get("city1")
        location2 = request.form.get("city2")


        coordinates1 = geocoder.geocode (location1)
        coordinates2 = geocoder.geocode (location2)


        lat1, long1 = (coordinates1. latitude), (coordinates1. longitude)
        lat2,long2 = (coordinates2.latitude), (coordinates2.longitude)
        placel = (lat1, long1)
        place2  =(lat2, long2)
        city = distance.distance(placel,place2)

        

        return render_template("index.html", box = city)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)