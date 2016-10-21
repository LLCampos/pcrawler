from flask import Flask, jsonify
import json

HOST = 'localhost'
PORT = 5001
DEBUG = False

app = Flask(__name__)

PDATA_FOLDER = 'pdata/'
PDATA_LASTUPDATE = 'last_update_date.json'
PDATA_COMPLETE = 'complete.json'


@app.route('/last_update', methods=['GET'])
def last_update():

    with open(PDATA_FOLDER + PDATA_LASTUPDATE) as last_update_file:
        last_update_dict = json.load(last_update_file)

    return jsonify(**last_update_dict)


@app.route('/passatempos', methods=['GET'])
def passatempos():

    with open(PDATA_FOLDER + PDATA_COMPLETE) as complete_pdata_file:
        complete_pdata_dict = json.load(complete_pdata_file)

    return jsonify(**complete_pdata_dict)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
