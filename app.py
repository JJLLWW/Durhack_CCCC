"""
Simple hello world
"""

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    return render_template("home.html")
