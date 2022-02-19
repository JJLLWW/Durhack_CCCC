"""
Simple hello world
"""

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    return render_template("home.html")
