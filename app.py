# in python default library already have sqlite3
import sqlite3

connect = sqlite3.connect('data.db')

connect.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, username TEXT, password TEXT)')

connect.close()
