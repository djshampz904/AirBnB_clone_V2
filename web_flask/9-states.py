#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states", strict_slashes=False)


def states():
    """ Display a HTML page: (inside the tag BODY) """
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)


def states_id(id):
    """ Display a HTML page: (inside the tag BODY) """
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """ Close the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
