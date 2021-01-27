import sqlite3 as lit

db = lit.connect('userdata.db')

with db:
    password = 'aaa'

    cur = db.cursor()
    cur.execute("DELETE FROM users WHERE password=?", (password,))
    db.commit()
    print("User data deleted successfully")

dbs = lit.connect('food.db')

with dbs:
    price = '5.00'

    cur = db.cursor()
    cur.execute("DELETE FROM food WHERE price=?", (price,))
    db.commit()
    print("Food data deleted successfully")