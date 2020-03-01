#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_():
    """Function for Flask Web Application"""
    states = {}
    s_states = {}
    alls = storage.all('State')
    # print(alls)
    for k, v in alls.items():
        name_of, id = k.split(".")[0], k.split(".")[1]
        name = v.to_dict()['name']
        states[id] = name

    for key, value in sorted(states.items(), key=lambda item: item[1]):
        s_states[key] = value
    # print("states ->>>>>", states)
    return render_template('7-states_list.html', nom="States", states=s_states)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
