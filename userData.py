import sqlite3 as lit

#define connection and cursor

connection = lit.connect('userdata.db')

cursor = connection.cursor()

#create username table

command1 = """CREATE TABLE IF NOT EXISTS 
users(username TEXT,password TEXT,name TEXT,email TEXT)"""

cursor.execute(command1)