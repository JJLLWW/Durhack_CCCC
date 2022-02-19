import database as db
import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
db.create_tables(cursor)

db.add_user( 'name2', 'pasass', 0, 'email.com', cursor)
db.add_user( 'name', 'pasass2', 0, 'email.com', cursor)
db.add_user( 'name', 'pasass2', 0, 'email.com', cursor)

db.add_message("user2", "user1", "text", cursor)
db.add_message("user1", "user2", "texts", cursor)
db.add_message("user1", "user2", "thi", cursor)
db.add_message("user2", "user1", "tfejn", cursor)
db.get_message("user1", "user2", cursor)

usr = db.get_user('name', cursor)
print(usr.all)