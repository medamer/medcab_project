from flask import Blueprint, jsonify
from .web_app.model import my_prediction

# home = Blueprint("home", __name__)

# @home.route("/")
# def index():
#     return "Hello World"

# @home.route("/predict")
# def predict():
#     sample = input('What do you need? ')
#     mylist = my_prediction(sample)
#     print(mylist)
#     return

# @home.route("/about")
# def about():
#     return "About me"

print(my_prediction('relax'))