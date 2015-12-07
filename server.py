from flask import Flask, request, render_template, redirect, flash, session
from jinja2 import StrictUndefined
# from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
    """Home page"""

    return render_template("index.html")


if __name__ == "__main__":
    
    PORT = int(os.environ.get("PORT", 5000))

    app.run(debug=True, host="0.0.0.0", port=PORT)
