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
    for table_name, table_creation_string in tables_creation_strings.items():
        print(table_name)
        mycursor.execute(table_creation_string)
    
    return "Stworzono tabele"


def drop_all_tables(con):
    with open("data\\parameters\\tables.json") as file:
        tables_creation_strings = json.load(file)
    mycursor = con.cursor()
    for table_name, table_creation_string in tables_creation_strings.items():
        #print(table_name)
        mycursor.execute("DROP TABLE " + table_name)
        print('Succesfully dropped' + table_name)
    return 'All tables are droped'

create_tables(create_connection())

input('z')
drop_all_tables(create_connection())


