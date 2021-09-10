import os

from flask import Flask, render_template

app= Flask(__name__)

# a simple page that renders a page
@app.route('/')
def index():
    return render_template('index.html')


