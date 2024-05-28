from dotenv import load_dotenv
import os
import mysql.connector
import json


def create_connection():
    load_dotenv()
    con = mysql.connector.connect(
        host="giniewicz.it",
        user=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('BASE')
    )

    if con:
        print("Połączenie udane")
    else:
        print("Połączenie nieudane")

    return con


def create_tables(con, statements):
    mycursor = con.cursor()
    try:
        for table_name, table_creation_string in statements.items():
            print(table_name)
            mycursor.execute(table_creation_string)
    except Exception as e:
        print(f'could not create table "{table}", {str(e)}')
        return
    print('tables successfully created')


def drop_all_tables(con, table_names):
    mycursor = con.cursor()
    try:
        for table_name in table_names:
            mycursor.execute("DROP TABLE IF EXISTS " + table_name)
            print('Successfully dropped ' + table_name)
    except Exception as e:
        print(f'could not create table "{table_name}", {str(e)}')
        return
    print("tables successfully dropped")


with open("parameters\\tables.json") as file:
    tables = json.load(file)["tables"]

create_statements = {}
for table in tables:
    with open(f"queries\\{table}.txt") as file:
        create_statements[table] = file.read()

create_tables(create_connection(), create_statements)

# drop_all_tables(create_connection(), tables[:: -1])

