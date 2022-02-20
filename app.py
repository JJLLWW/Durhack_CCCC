"""
Simple hello world, on branch
"""
from base64 import urlsafe_b64decode
import database as db
import sqlite3
from socket import SocketIO, socket
from flask import Flask, flash, redirect, render_template, request, session, url_for
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from assistingFunctions import login_required
from database import verify_user, errmsg_from_code, add_user
from flask_socketio import SocketIO

language = {
    "English ": 1,
    "French": 2,
    "Spanish": 3,
    "Russian": 4
}

con = sqlite3.connect("database.db", check_same_thread=False)
cursor = con.cursor()
db.create_tables(cursor)
app = Flask(__name__)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b'P\x87\xfc\xa9\xe6qQ~)8\x90D\x11\n\xb9\xa1'
Session(app)
sio = SocketIO(app)


db.add_user("jack wright", "pass", "none", 0, "jackwright@gmail.com", cursor)

@app.route("/", methods=["GET","POST"])
@login_required
def index():
    return render_template("home.html")

""" @socketio.on('join_chat')
def join():
    print("use")

@socketio.on('msg_sent')
def msg_sent(body):
    print("sent message", str(body)) """

@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    if request.method == "POST":
        return redirect("/chat")
    else:
        """Call on messages.db table"""
        return render_template("chat.html")

@app.route("/changePassword", methods=["GET", "POST"])
@login_required
def changePassword():
    if request.method == "POST":
        password = request.form.get("password")
        confirmPass = request.form.get("confirmation")
        if not password or not confirmPass:
            flash("Please enter password(s)")
            return redirect("/changePassword")
        if password == confirmPass:
            flash("Changes saved.")
            """Update user db"""
            return redirect("/")
        else:
            flash("Please ensure password and confirm-password match.")
            return redirect("/register")
    else:
        return render_template("changePassword.html")

@app.route("/helpSettings", methods=["GET", "POST"])
@login_required
def help():
    if request.method == "POST":
        prefs = request.form.get("myTags")
        lang = language[request.form.get("language")]
        """Ammend user details"""
        flash("Changes saved.")
        return redirect("/")
    else:
        """get user from database and pass in variables, for language and prefs"""
        return render_template("help.html", language=language, prefs=prefs)

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
        verification = "USER FOUND"
        #verify_user(username, password, cursor)
        if verification == "USER FOUND":
            flash("Welcome back " + username + "!")
            session["username"] = username
            return redirect("/")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Please enter a correct username")
            return redirect("/register")
        password = request.form.get("password")
        confirmPass = request.form.get("confirmation")
        if not password or not confirmPass:
            flash("Please enter password(s)")
            return redirect("/register")
        email = request.form.get("email")
        prefs = request.form.get("myTags")
        lang = request.form.get("language")
        langId = language[lang]
        if password == confirmPass:
            add_user(username, password, prefs, langId, email, cursor)
        else:
            flash("Please ensure password and confirm-password match.")
            return redirect("/register")
    else:
        return render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    """ Log user out """
    flash("Logged out.")
    session.clear()
    return redirect("/login")

@sio.on('msg_sent')
def on_msg_sent(json):
    txt = json['msg_txt']
    sio.emit('msg_from_serv', {'text': txt})

app.run()