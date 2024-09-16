from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from security import authenticate, identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "something"  # Change this!
api = Api(app)

jwt = JWTManager(app)

items = []


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = authenticate(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)


@jwt.user_identity_loader
def user_identity_lookup(user_id):
    return user_id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return identity({"identity": identity})


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            items.remove(item)
            return {"message": "Item deleted"}
        return {"message": "Item not found"}, 404

    @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(request.get_json())
            return item
        return {"message": "Item not found"}, 404


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    app.run(port=6000, debug=True)
