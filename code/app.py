from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item

    def delete(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            items.remove(item)
            return {"message": "Item deleted"}
        return {"message": "Item not found"}, 404

    def put(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(request.get_json())
            return item
        return {"message": "Item not found"}, 404


api.add_resource(Item, "/item/<string:name>")

if __name__ == "__main__":
    app.run(port=6000, debug=True)
