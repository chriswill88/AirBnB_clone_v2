#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states_list')
def state_():
    """Function for Flask Web Application"""
    states = {}
    alls = storage.all('State')
    # print(alls)
    for k, v in alls.items():
        name_of, id = k.split(".")[0], k.split(".")[1]
        name = v.to_dict()['name']
        # print(name, name_of)
        states[id] = name
        # print("states ->>>>>", states)
    return render_template('7-states_list.html', nom="States", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
