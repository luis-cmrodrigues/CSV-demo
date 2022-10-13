from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Initial list of Fruits, feel free to replace any of them.
FRUITS = {
    '1': {'name': '--- Enter your favorite fruit here ---'},
    '2': {'name': 'Apple'},
    '3': {'name': 'Pear'},
    '4': {'name': 'Watermelon'},
    '5': {'name': 'Banana'},
    '6': {'name': 'Strawberry'}
  }

class FruitsList(Resource):
    # return current list of fruits
    def get(self):
        return FRUITS

    # adds a new fruit
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        args = parser.parse_args()
        fruit_id = int(max(FRUITS.keys())) + 1
        fruit_id = '%i' % fruit_id
        FRUITS[fruit_id] = {
            "name": args["name"]            
        }
        return FRUITS[fruit_id], 201

class Fruit(Resource):
    # get a single fruit by fruit Id
    def get(self, fruit_id):
        if fruit_id not in FRUITS:
            return "Not found", 404
        else:
            return FRUITS[fruit_id]

# register resources
api.add_resource(FruitsList, '/fruits/')
api.add_resource(Fruit, '/fruits/<fruit_id>')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)