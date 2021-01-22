import pandas as pd
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


query = """
        select strain_name as Name, strain_type as Type, strain_rating as Rating, 
                strain_effects as Effects, strain_description as Description, 
                strain_flavors as Flavors from medcab
            WHERE
                strain_id in(100,120,150, 340, 680)
        order by strain_rating desc;
        """
cursor.execute(query)
myresult = cursor.fetchall()

print(myresult.dtype())

