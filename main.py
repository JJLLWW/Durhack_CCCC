import database as db
import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
db.create_tables(cursor)

db.add_user(0, 'name2', 'pasass', 0, 'email.com', cursor)
db.add_user(0, 'name', 'pasass2', 0, 'email.com', cursor)
db.add_user(0, 'name', 'pasass2', 0, 'email.com', cursor)

usr = db.get_user('name', cursor)
print(usr.all)