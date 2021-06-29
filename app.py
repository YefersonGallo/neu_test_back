from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from database import Connection

app = Flask(__name__)
CORS(app, support_credentials=True)

conn = Connection()


@app.route('/city', methods=['POST'])
@cross_origin(supports_credentials=True)
def city():
    body = request.json
    return jsonify(conn.get_population_by_city(body["city"]))


@app.route('/state', methods=['POST'])
@cross_origin(supports_credentials=True)
def state():
    body = request.json
    return jsonify(conn.get_population_by_state(body["state"]))


@app.route('/country', methods=['POST'])
@cross_origin(supports_credentials=True)
def country():
    body = request.json
    return jsonify(conn.get_population_by_country(body["country"]))


if __name__ == '__main__':
    app.run(debug=False)
