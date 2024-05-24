from dotenv import load_dotenv
import os
import mysql.connector
import json

def create_connection():
    load_dotenv()
    con = mysql.connector.connect(
    host = "giniewicz.it",
    user = os.getenv('LOGIN'),
    password = os.getenv('PASSWORD'),
    database = os.getenv('BASE')
)

    if(con):
        print("Połączenie udane")
    else:
        print("Połączenie nieudane")

    return con

def create_tables(con):
    with open("data\\parameters\\tables.json") as file:
        tables_creation_strings = json.load(file)
    
    mycursor = con.cursor()

    #mycursor.execute(tables_creation_strings["Test"])
    
    return "Stworzono tabele"