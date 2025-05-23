import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password123"


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return "Login successful"
    else:
        return "Login failed"


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    file.save(os.path.join("/uploads", file.filename))

    return "File uploaded"


@app.route("/command", methods=["POST"])
def command():
    cmd = request.form["cmd"]
    os.system(cmd)

    return "Command executed"


if __name__ == "__main__":
    app.run(debug=True)
