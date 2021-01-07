from flask import Blueprint, jsonify

home = Blueprint("home", __name__)

@home.route("/")
def index():
    return "Hello World"

@home.route("/predict")
def predict():
    mytext = "This is a prediction page"
    return jsonify(mytext)

@home.route("/about")
def about():
    return "About me"