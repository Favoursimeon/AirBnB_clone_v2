#!/usr/bin/python3

""" starts a Flask web application"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ display Hello HBNB! """
    if request.path == '/':
        return 'Hello HBNB!'
    elif request.path == '/hbnb':
        return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ display C followed by the value of the text variable """
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
