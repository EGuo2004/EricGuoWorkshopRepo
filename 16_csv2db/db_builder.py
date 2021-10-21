#The Adjective Nouns: Noakai Aronesty, Andrew Juang, Eric Guo
#SoftDev
#K16 -- All About Database
#2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

with open('courses.csv', newline='') as csvfile0:
    readerC = csv.DictReader(csvfile0) #reads courses.csv
    command = ""          # test SQL stmt in sqlite3 shell, save as string
    c.execute(command)    # run SQL statement
    c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER);") #Creates a table named courses if it doesn't already exist, the columns are a TEXT column code, and two INTEGER columns mark and id
    for row in readerC: #for every row in the file read, it will make a new row inserting information in the appropriate columns. 
        c.execute("INSERT INTO courses VALUES (\"" +row['code']+ "\"," +row['mark']+"," +row['id']+ ");")
with open('students.csv', newline='') as csvfile1:
    readerS = csv.DictReader(csvfile1) #reads students.csv
    c.execute(command)    # run SQL statement
    c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER);") #Creates a table named students if it doesn't already exist, with a TEXT column name, and two INTEGER columns age and id
    for row in readerS: #for every row in the file read, it will make a new row inserting information in the appropriate columns
        c.execute("INSERT INTO students VALUES (\"" +row['name']+ "\"," +row['age']+"," +row['id']+ ");")

#TESTING courses import:
c.execute("SELECT * FROM courses")
colnames = c.description
for line in colnames:
    print(line[0])
rows = c.fetchall()
for row in rows:
    print(row)

print("\n\n")
#TESTING students import:
c.execute("SELECT * FROM students")
colnames = c.description
for line in colnames:
    print(line[0])
rows = c.fetchall()
for row in rows:
    print(row)
#==========================================================

db.commit() #save changes
db.close()  #close database
