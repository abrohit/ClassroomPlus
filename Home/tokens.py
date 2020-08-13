from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.crypto import get_random_string
import uuid

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

#class SessionGenerator(PasswordResetTokenGenerator):
#    def _make_hash_value(self, user, timestamp):
#        return (
#            text_type(user.pk) + text_type(timestamp) +
#            text_type(user.password)
#        )
#session_activation_token = SessionGenerator()
