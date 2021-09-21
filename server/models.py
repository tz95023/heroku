# server/models.py

from server.database import db
from server.encryption import bcrypt
import datetime
# from server import app
# from server.database import db


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, rounds, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, rounds
        ).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        # rounds = app.config.get('BCRYPT_LOG_ROUNDS')