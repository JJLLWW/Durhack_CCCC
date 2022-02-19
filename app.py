"""
Simple hello world
"""

from socket import SocketIO, socket
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO
from flask_session import Session
import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["GET","POST"])
def hello_world():
    return render_template("chat.html")

@socketio.on('join_chat')
def join():
    print("use")

@socketio.on('msg_sent')
def msg_sent(body):
    print("sent message", str(body))

if __name__ == "__main__":
    app.run()