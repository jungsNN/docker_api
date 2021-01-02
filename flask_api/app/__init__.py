import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("states.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # convert to HTML
        return markdown.markdown(content)

class FipsList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        fips = []

        for key in keys:
            fips.append(shelf[key])

        return {'message':'Success', 'data': fips}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argment('total_open', required=True)
        parser.add_argment('status', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'State registered', 'data': args}, 201

class State(Resource):
    def get(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error
        if not (identifier in shelf):
            return {'message': 'State data not found', 'data': {}}, 404
        return {'message': 'State data found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error
        if not (identifier in shelf):
            return {'message': 'State data found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204

api.add_resource(FipsList, '/fips')
api.add_resource(State, '/fips/<state>')
