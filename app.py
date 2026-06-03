from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'avens_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avens.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120))
    password = db.Column(db.String(200))

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/consistency")
def consistency():
    return render_template("consistency.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/ai")
def ai():
    return render_template("ai_assistant.html")

@app.route("/internships")
def internships():
    return render_template("internship.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
