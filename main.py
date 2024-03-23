from flask import Flask
from api.router import index, get_items, add_item

app = Flask(__name__)


@app.route("/")
def home():
    return index()


@app.route("/getitems", methods=["GET"])
def get_items_route():
    return get_items()


@app.route("/additems", methods=["POST"])
def add_item_route():
    return add_item()


if __name__ == "__main__":
    app.run(debug=True)
