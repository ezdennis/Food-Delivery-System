import sqlite3 as lit

db = lit.connect('userdata.db')

with db:
    password = 'aaa'

    cur = db.cursor()
    cur.execute("DELETE FROM users WHERE password=?", (password,))
    db.commit()
    print("Data deleted successfully")

