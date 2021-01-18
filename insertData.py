import sqlite3 as lit

myusers = (
    (1, 'Kelvin', '123', 'Kelvin Teo', '0123456789', 'kampung raja'),
    (2, 'John', '123', 'Johnson Ng', '0123456789', 'tringkap'),
    (3, 'Xzx', '123', 'Xiao Zhu', '0123456789', 'kuala terla'),
    (4, 'Jason', '123', 'Jason Lu', '0123456789', 'blue valley'),

)

db = lit.connect('user.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?,?,?,?)', myusers)

    print("Data inserted successfully")
