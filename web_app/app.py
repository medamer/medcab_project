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
DB_NAME = os.getenv("NAME")
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

    # in({pred[0]},{pred[1]},{pred[2]}, {pred[3]}, {pred[4]})

    query = f"""
            select strain_name, strain_type, strain_rating, 
	               strain_effects, strain_description, 
	               strain_flavors from medcab
                WHERE
                    strain_id = {pred}
            order by strain_rating desc;
            """
    cursor.execute(query)
    myresult = cursor.fetchall()

    #df = pd.DataFrame(myresult, columns=['Name', 'Type', 'Rating', 'Effects', 'Description', 'Flavors'])
    pred=myresult[0][0]
    pred1=myresult[0][1]
    pred2=myresult[0][2]
    pred3=myresult[0][3]
    pred4=myresult[0][4]
    pred5=myresult[0][5]

    return render_template('prediction.html', pred=pred, pred1=pred1, pred2=pred2,
                                              pred3=pred3, pred4=pred4, pred5=pred5)

if __name__ == '__main__':
    #app.debug = True
    app.run()