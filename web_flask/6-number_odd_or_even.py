#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template

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


@app.route('/number/<int:n>')
def numfun(n):
    """Function for Flask Web Application"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template(n):
    """Function for Flask Web Application"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def oddeven(n):
    """Function for Flask Web Application"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
