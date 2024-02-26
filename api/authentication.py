from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        if email is None or password is None:
            return None
        
        try:
            user = UserModel.objects.get(email=email)
            print(user)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
