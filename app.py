"""
Simple hello world, on branch
"""
import database as db
import sqlite3
from socket import SocketIO, socket
from flask import Flask, flash, redirect, render_template, request, session, url_for
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from assistingFunctions import login_required
from database import verify_user, errmsg_from_code

con = sqlite3.connect("database.db")
cursor = con.cursor()
db.create_tables(cursor)
app = Flask(__name__)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b'P\x87\xfc\xa9\xe6qQ~)8\x90D\x11\n\xb9\xa1'
Session(app)

@app.route("/", methods=["GET","POST"])
@login_required
def index():
    if request.method == "POST":
        pass
    else:
        render_template("home.html")

""" @socketio.on('join_chat')
def join():
    print("use")

@socketio.on('msg_sent')
def msg_sent(body):
    print("sent message", str(body)) """

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Please enter a correct username")
            return redirect("/login")
        password = request.form.get("password")
        if not password:
            flash("Please enter a password")
            return redirect("/login")
        print(username, password)
        verification = verify_user(username, password, cursor)
        if verification == "USER FOUND":
            pass
    else:
        return render_template("login.html")

app.run()