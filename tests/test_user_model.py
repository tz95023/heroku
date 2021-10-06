# server/tests/test_user_model.py

import unittest

from server.database import db
from server.models import User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def encode_auth(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        return auth_token

    def test_encode_auth_token(self):
        auth_token = self.encode_auth()
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        auth_token = self.encode_auth()
        self.assertTrue(isinstance(auth_token, str))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)

if __name__ == '__main__':
    unittest.main()
