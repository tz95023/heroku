# server/__inti__.py


import os
# import click
import server.database
import server.encryption
import server.commands
import server.migration
import server.config
import sys
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

#print(os.getenv("SECRET_KEY"))

app = Flask(__name__)
CORS(app)

load_dotenv()

flask_app = os.getenv('FLASK_APP')
if flask_app is None:
    flask_app = os.environ.get('FLASK_APP')
app_settings = os.getenv('APP_SETTINGS')
if app_settings is None:
    app_settings = os.environ.get('APP_SETTINGS')

app.config.from_object(app_settings)
server.config.current_BCRYPT_LOG_ROUNDS = app.config['BCRYPT_LOG_ROUNDS']
#print(app.config["SECRET_KEY"])

#print(server.config.current_BCRYPT_LOG_ROUNDS)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:953515@localhost:5433/da-flask-app'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)
database.init_app(app)
encryption.init_app(app)

commands.init_app(app)
migration.init_app(app)
#migrate = Migrate(app, db)

from server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)
# @app.cli.command("create-db")
#def create_db():
#    db.create_all

# a simple page that renders a page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app_settings')
def app_settings():
    return render_template('app_settings.html', database_uri=app.config['SQLALCHEMY_DATABASE_URI'])


