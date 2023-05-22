#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
#connecting to database
conn=sqlite3.connect("pets.db")

#creating tables
conn.execute('''CREATE TABLE person(
id INT PRIMARY KEY NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INT NOT NULL);''')

conn.execute('''CREATE TABLE pet(
id INT PRIMARY KEY,
name TEXT,
breed TEXT,
age INT,
dead INT);''')

conn.execute('''CREATE TABLE person_pet(
person_id INT,
pet_id INT);''')

#DO NOT CREATE pets.db separately. It will be created automatically.
cur=conn.cursor()
#inserting data into person table
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (1,'James','Smith',41);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (2,'Diana','Greene',23);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (3,'Sara','White',27);")
cur.execute("INSERT INTO person (id,first_name,last_name,age) VALUES (4,'William','Gibson',23);")
#inserting data into pet table
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (1,'Rusty','Dalmation',4,1);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (2,'Bella','AlaskanMalamute',3,0);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (3,'Max','CockerSpaniel',1,0);")
cur.execute("INSERT INTO pet (id,name,breed,age,dead) VALUES (6,'Spot','Bloodhound',2,1);")
#inserting data into person_pet table
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (1,2);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (2,3);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (2,4);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (3,5);")
cur.execute("INSERT INTO person_pet (person_id,pet_id) VALUES (4,6);")
conn.commit()
conn.close()
query_pets.py

import sqlite3
#connecting to database
conn=sqlite3.connect("pets.db")
cur=conn.cursor()

#function to print person details
def print_person(person_id:int,cur):
    try:
        data=cur.execute(f'SELECT * FROM person WHERE id={person_id}')
        data=list(data)
        print(f"{data[0][1]} {data[0][2]}, {data[0][3]} years old")
        pet_id_sql=cur.execute(f'SELECT * FROM person_pet WHERE person_id={person_id}')
        pet_ids=list(pet_id_sql)
        for i in range(len(pet_ids)):
            pet_data=cur.execute(f'SELECT * FROM pet WHERE id={pet_ids[i][1]}')
            pet_data=list(pet_data)
            if(pet_data!=[]):
                if(pet_data[0][4]==0):
                    print(f"{data[0][1]} {data[0][2]} owns {pet_data[0][1]},a {pet_data[0][2]},that is {pet_data[0][3]} years old.")
                else:
                    print(f"{data[0][1]} {data[0][2]} owned {pet_data[0][1]},a {pet_data[0][2]},that was {pet_data[0][3]} years old.")
    except:
        print("ERROR! Person id not found! Try Again!")
    

while(True):
    person_id=input("Enter person id number:")
    if(person_id !="a1"):
        person_id=int(person_id)
        print_person(person_id,cur)
    else:
        break

