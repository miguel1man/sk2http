from flask import Flask
from api.router import add_item, get_items, index, sk_get

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


@app.route("/sk_get", methods=["POST"])
def sk_get_route():
    return sk_get()


if __name__ == "__main__":
    app.run(debug=True)
