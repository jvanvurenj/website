
import flask
#import config
from flask import request
#import logging
# import geocoder
#import requests

# Globals
app = flask.Flask(__name__)
#CONFIG = config.configuration()
#app.secret_key = CONFIG.SECRET_KEY
#app.debug = CONFIG.DEBUG


# Pages
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Home page")
    return flask.render_template('index.html')


# Error handlers
@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


if __name__ == "__main__":
    app.run(debug=True)
