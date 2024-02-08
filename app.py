import postgresqlite
from flask import Flask, request, render_template, redirect, url_for, flash, session

from forms import TestForm
from models import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = postgresqlite.get_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


# Create tables based on the Model classes.
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
