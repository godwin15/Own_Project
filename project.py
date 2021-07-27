from turbo_flask import Turbo
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f799add3db9d9cb7f9edccbb37e1d256'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)