#!/usr/bin/python3

""" starts a Flask web application"""
from flask import Flask, request, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ display Python followed by the value of the text variable """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_n(n):
    """ display n is a number only if n is an integer """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ display a HTML page only if n is an integer """

    filename = '6-number_odd_or_even.html'
    if n % 2 == 0:
        return render_template(filename, n=n, odd_or_even='even')
    else:
        return render_template(filename, n=n, odd_or_even='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
