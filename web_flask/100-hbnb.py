#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_filters():
    states = storage.all("State")
    cities = storage.all("City")
    amenities = storage.all("Amenity")
    places = storage.all("Place")

    return render_template("100-hbnb.html",
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
