# server/__inti__.py


import os
# import click
import server.database
import server.encryption
import server.commands
import server.migration
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:953515@localhost:5433/da-flask-app'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)
database.init_app(app)
encryption.init_app(app)

commands.init_app(app)
migration.init_app(app)
#migrate = Migrate(app, db)


# @app.cli.command("create-db")
#def create_db():
#    db.create_all

# a simple page that renders a page
@app.route('/')
def index():
    return render_template('index.html')


