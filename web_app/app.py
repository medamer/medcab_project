import pandas as pd
from model import my_prediction
from flask import Flask, render_template, request
from dotenv import load_dotenv
import psycopg2
import os
from psycopg2.extras import execute_values


# Load dotenv
load_dotenv()

# Get the credentials from .env file:
DB_USER = os.getenv("USER")
DB_NAME = os.getenv("USER")
DB_PASSWORD = os.getenv("PASSWORD")
DB_HOST = os.getenv("SERVER")

# Connect to the Database:
connection = psycopg2.connect(dbname=DB_USER, user=DB_NAME, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    user_input = request.form['comment']
    pred = my_prediction(user_input)
    query = f"""
            select strain_name as Name, strain_type as Type, strain_rating as Rating, 
	               strain_effects as Effects, strain_description as Description, 
	               strain_flavors as Flavors from medcab
                WHERE
                    strain_id in({pred[0]},{pred[1]},{pred[2]}, {pred[3]}, {pred[4]})
            order by strain_rating desc;
            """
    cursor.execute(query)
    myresult = cursor.fetchall()

    return render_template('prediction.html', predicted=myresult)

if __name__ == '__main__':
    app.debug = True
    app.run()