import json
from flask import jsonify, request

items = []


def index():
    return "Semantic Kernel API 0.0.1"


def get_items():
    return jsonify(items)


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
