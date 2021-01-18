import sqlite3 as lit

db = lit.connect('userdata.db')

#markup the login user as customer or restaurant admin

with db:
    updateField = "customer"
    username = "kelvin"

    cur = db.cursor()
    cur.execute('UPDATE users SET field = ? WHERE username=?', (updateField, username))
    db.commit()
    print("Data updated successfully")




