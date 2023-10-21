#!/usr/bin/python3
"""get cities by states"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(exception):
    storage.close()


@app.route('//cities_by_states', strict_slashes=False)
def display_cities():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
