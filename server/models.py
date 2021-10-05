# server/models.py

from server.database import db
from server.encryption import bcrypt
import server.config
import datetime
import jwt
import sys
import os
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

    def __init__(self, email, password, admin=False):


        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, server.config.current_BCRYPT_LOG_ROUNDS
        ).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        # rounds = app.config.get('BCRYPT_LOG_ROUNDS')

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e