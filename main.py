import json
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []


@app.route("/")
def index():
    return "Welcome to the item API!"


@app.route("/getitems", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/additems", methods=["POST"])
def add_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"data received:\n{data}")

    if isinstance(data, str):
        print(f"data isinstance: {data}")

    data_fixed = data.replace("'", '"')
    data_dict = json.loads(data_fixed)

    if not isinstance(data_dict, dict):
        print(f"data error: {data_dict}")
        return jsonify({"error": "Invalid JSON data"}), 400

    item = {
        "id": 1,
        "title": data_dict["title"],
        "description": data_dict.get("description", ""),
    }
    items.append(item)
    return jsonify(data_dict), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    for item in items:
        if item["id"] == item_id:
            data = request.get_json()
            item["title"] = data.get("title", item["title"])
            item["description"] = data.get("description", item["description"])
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)
