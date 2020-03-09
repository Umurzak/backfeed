import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    """Sign up for Backfeed"""

    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")
    db.execute("INSERT INTO users (name, password) VALUES (:name, :password)", {"name": name, "password": password})
    db.commit()
    return render_template("success.html")

@app.route("/log", methods=["POST", "GET"])
def log():
    return render_template("login.html")

@app.route("/logged", methods=["POST"])
def logged():
    """Backfeed Log in"""
    namelog = request.form.get("namelog")
    passwordlog = request.form.get("passwordlog")
    if db.execute("SELECT * FROM users WHERE name = :name", {"name": namelog}).rowcount == 0:
        return render_template("error.html", message="Wrong username or password")
    if db.execute("SELECT * FROM users WHERE password = :password", {"password": passwordlog}).rowcount == 0:
        return render_template("error.html", message="Wrong username or password")
    return render_template("logged.html")
