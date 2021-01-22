import os
import pandas as pd
import numpy as np
from os.path import join, dirname
from dotenv import load_dotenv
import csv
import json
import psycopg2
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
print('CONNECTED')

# # Create our table:
# query = """
#         CREATE TABLE IF NOT EXISTS medcab (
#             strain_id SERIAL PRIMARY KEY,
#             strain_name varchar(1000),
#             strain_type varchar(100),
#             strain_rating float,
#             strain_effects varchar(20000),
#             strain_description varchar(20000),
#             strain_flavors varchar(1000),
#             strain_nearest varchar(1000)
#         ) """
# cursor.execute(query)
# connection.commit()
# print("Table Created")

# # Read the csv file:
# file_path =  './data/cannabis_new.csv' #os.path.join(os.path.dirname(__file__), "../cannabis_new.csv")
# df = pd.read_csv(file_path)
# psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# # Load the csv file to the database:
# list_of_tuples = list(df.to_records(index=False))

# insert_query = """
#                 INSERT INTO medcab(
#                     strain_id, strain_name, strain_type, strain_rating, strain_effects, strain_description,
#                     strain_flavors, strain_nearest
#                 ) VALUES %s ;
#                 """

# execute_values(cursor, insert_query, list_of_tuples)
# connection.commit()


# Check the table:
query2 = """ SELECT * FROM testtab """
cursor.execute(query2)
myresult = cursor.fetchall()

for x in myresult:
    print(x)


cursor.close()
connection.close()
print('DISCONNECTED')