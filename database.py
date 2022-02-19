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
    cursor.execute("""
        SELECT NAME FROM USER where NAME = ?
    """, [Name])
    # if there is an entry already we don't do anything
    for row in cursor:
        return
    cursor.execute("""
    INSERT INTO USER (USERID, NAME, PASSWORD, LANGUAGEID, EMAIL) VALUES(?, ?, ?, ?, ?)
    """, [Id, Name, Pass, Langid, Email])  

#add_user(234, "Olivia", "olivia", "45456", "@olivia.com")   
add_user(0, 'name2', 'pasass', 0, 'email.com')
add_user(0, 'name', 'pasass2', 0, 'email.com')
add_user(0, 'name', 'pasass2', 0, 'email.com')


def get_user(name):
    cursor.execute("""
        SELECT * FROM USER where NAME = ?
    """, [name])
    result = ""
    for row in cursor:
        newusr = user(row[0], row[1], row[2], row[3], row[4])
        return newusr

SUCCESS, ERR_NOUSR, ERR_WRONGPASS = 0, 1, 2
def errmsg_from_code(code):
    if code == SUCCESS:
        print("success")
    elif code == ERR_NOUSR:
        print("no user")
    elif code == ERR_WRONGPASS:
        print("wrong password")

def verify_user(name, password):
    real_password = None
    cursor.execute("""
        SELECT NAME FROM USER where NAME = ?
    """, [name])
    print(name)
    for row in cursor:
        # if the name exists, check the password
        print("exist")
        exist_name = (row)
        cursor.execute("""
        SELECT PASSWORD FROM USER where NAME = ?
        """, [name])
        for row in cursor:
            real_password = row[0]
            print(f"password was {real_password}")
        if password == real_password:
            return SUCCESS
        else:
            return ERR_WRONGPASS
    return ERR_NOUSR

code = verify_user("name2", "pasass")
errmsg_from_code(code)

#usr = get_user("name2")
#print(usr.all)

