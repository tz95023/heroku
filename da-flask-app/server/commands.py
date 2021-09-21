# server/commands.py


# from server import app
from server.database import db
from server.models import User
import click


def do_something():
        print("ola kala!")

def create_db():
    db.create_all()

def drop_db():
    db.drop_all()

def create_user_table():
    User.__table__.create(db.engine)

def init_app(app):
    for command in [create_db, drop_db, create_user_table, do_something]:
        app.cli.add_command(app.cli.command()(command))        

