import sqlite3

def createDatabase():
    connection = sqlite3.connect("data/kalshi.db")

    with open("src/database/schema.sql", "r") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.close()

createDatabase()