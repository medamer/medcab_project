import pandas as pd
from web_app.model import my_prediction
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    user_input = request.form['comment']
    pred = my_prediction(user_input)
    return render_template('prediction.html', data=pred)

if __name__ == '__main__':
    app.debug = True
    app.run()