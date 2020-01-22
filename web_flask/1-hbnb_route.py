#!/usr/bin/python3
from flask import Flask
"""Modual For Simple Flask"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function for Flask Web Application"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Function for Flask Web Application"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
