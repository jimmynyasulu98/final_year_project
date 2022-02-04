""" module contains all functions to query and store updates into
the database"""

import sqlite3
from datetime import datetime

CREATE_UPDATE_TABLE = "CREATE TABLE IF NOT EXISTS updates (id INTEGER PRIMARY KEY, update_type TEXT, " \
                      "status TEXT, date DATETIME );"

INSERT_UPDATE = "INSERT INTO updates (update_type,status,date) VALUES (?,?,?);"
GET_ALL_UPDATES = "SELECT * FROM updates;"
GET_UPDATE_BY_NAME = "SELECT * FROM updates WHERE name =?;"


def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_UPDATE_TABLE)


def insert_update(connection, update_type, status, date):
    with connection:
        connection.execute(INSERT_UPDATE, (update_type, status, date))


def get_all_updates(connection):
    with connection:
        return connection.execute(GET_ALL_UPDATES).fetchall()


def get_update_by_name(connection, name):
    with connection:
        connection.execute(GET_UPDATE_BY_NAME, (name,))
