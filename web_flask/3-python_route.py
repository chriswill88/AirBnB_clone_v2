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


@app.route('/c/<text>')
def cisfun(text):
    """Function for Flask Web Application"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def pisfun(text="is_cool"):
    """Function for Flask Web Application"""
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
