import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
db = SQLAlchemy(app)

# a simple page that renders a page
@app.route('/')
def index():
    return render_template('index.html')


