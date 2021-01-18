import sqlite3 as lit

#define connection and cursor

connection = lit.connect('userdata.db')

cursor = connection.cursor()

#add 1 more attribute to the table

addColumn = "ALTER TABLE users ADD COLUMN field TEXT"

cursor.execute(addColumn)