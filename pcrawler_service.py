from flask import Flask, jsonify, make_response, request, current_app
import json
from datetime import timedelta
from functools import update_wrapper


# http://flask.pocoo.org/snippets/56/
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


HOST = 'localhost'
PORT = 5001
DEBUG = False

app = Flask(__name__)

PDATA_FOLDER = 'pdata/'
PDATA_LASTUPDATE = 'last_update_date.json'
PDATA_COMPLETE = 'complete.json'


@app.route('/last_update', methods=['GET'])
@crossdomain(origin='*')
def last_update():

    with open(PDATA_FOLDER + PDATA_LASTUPDATE) as last_update_file:
        last_update_dict = json.load(last_update_file)

    return jsonify(**last_update_dict)


@app.route('/passatempos', methods=['GET'])
@crossdomain(origin='*')
def passatempos():

    with open(PDATA_FOLDER + PDATA_COMPLETE) as complete_pdata_file:
        complete_pdata_dict = json.load(complete_pdata_file)

    return jsonify(**complete_pdata_dict)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
