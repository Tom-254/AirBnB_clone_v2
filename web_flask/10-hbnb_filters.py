#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    amenities_objs = storage.all("Amenity")

    return render_template("10-hbnb_filters.html",
            states=[value  for value in state_obj.values()],
            cities=[value  for value in city_obj.values()],
                           amenities=[value  for value in amenities_objs.values()])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
