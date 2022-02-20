from flask import redirect, render_template, request, session
from functools import wraps
from googletrans import Translator
trans = Translator()
# Assisting Functions - decorated functions
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def translateThis(string, target, source=None):
    text = string
    if source == None:
        return trans.translate(text, dest=target).text
    return trans.translate(string, dest=target, src=source).text

print(translateThis("hello", "es", "en"))