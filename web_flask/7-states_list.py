#!/usr/bin/python3
"""listing all states from database using flask."""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
