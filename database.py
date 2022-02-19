from ast import Pass
from collections import namedtuple
import sqlite3
import database2 as db2

con = sqlite3.connect("database.db")

cursor = con.cursor()

db2.create_tables(cursor)

class user:
    def __init__(self, id, name, password, langid, email):
        self.id = id
        self.name = name
        self.Pass = password
        self.langid = langid
        self.email = email
        self.all = [self.id, self.name, self.Pass, self.langid, self.email]

def add_user(Id, Name, Pass, Langid, Email):
    exist_name = ""
    cursor.execute("""
        SELECT NAME FROM USER where NAME = ?
    """, [Name])
    for row in cursor:
        exist_name = (row[0])
    if exist_name != "":
        cursor.execute("""
        INSERT INTO USER (USERID, NAME, PASSWORD, LANGUAGEID, EMAIL) VALUES(?, ?, ?, ?, ?)
        """, [Id, Name, Pass, Langid, Email])  
        print("Done")
    else:
        print("already exists")
    
#add_user(234, "Olivia", "olivia", "45456", "@olivia.com")   
add_user(0, 'name2', 'pasass', 0, 'email.com')
add_user(0, 'name', 'pasass2', 0, 'email.com')

def get_user(name):
    cursor.execute("""
        SELECT * FROM USER where NAME = ?
    """, [name])
    result = ""
    for row in cursor:
        newusr = user(row[0], row[1], row[2], row[3], row[4])
        return newusr

def verify_user(name, password):
    exist_name = ""
    real_password = ""
    cursor.execute("""
    SELECT NAME FROM USER where NAME = ?
    """, [name])
    print(name)
    for row in cursor:
        print("in")
        exist_name = (row[0])
    print(exist_name)
    if exist_name != "":
        print("exist")
        cursor.execute("""
        SELECT NAME FROM USER where PASSWORD = ?
        """, [password])
        print(password)
    else:
        return False
        print("no")

verify_user("name2", "pasass")


#usr = get_user("name2")
#print(usr.all)

print("hiiiiiiii")

