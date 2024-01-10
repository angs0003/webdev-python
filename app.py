# in python default library already have sqlite3
import sqlite3

connect = sqlite3.connect('data.db')

connect.execute('DROP TABLE IF EXISTS customer')
connect.execute('CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL)')

# connect.execute('INSERT INTO customer (NAME, AGE) VALUES ("John", 22)')
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

#one way to insert data
for item in data:
    connect.execute('INSERT INTO customer (NAME, AGE) VALUES (?, ?)', item)

# another way to insert data
# connect.executemany('INSERT INTO customer (NAME, AGE) VALUES (?, ?)', data)   
all_data = connect.execute('SELECT * FROM customer').fetchall()
# print(all_data)

connect.close()


##################
# Django API 
##################

import requests 
import json

response = requests.get("https://api.tomitokko.repl.co/")

# print(response.status_code)

# print(response.text)

# for res in response.text:
#     print(res)

res = json.loads(response.text)

# for data in res:
    # print(data)

###########################
    # OOP
###########################
class Person:
    name = 'Ren'
    age = 23

    def random(self):
        print("My name is ", self.name)
        print("My age is ", self.age)

demo = Person()

print(demo.age)
demo.random()