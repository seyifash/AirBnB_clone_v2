#!/usr/bin/python3
"""get states by id"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """ HBNB filters """
    states = storage.all(State).values()

    amenities = storage.all(Amenity).values()

    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
