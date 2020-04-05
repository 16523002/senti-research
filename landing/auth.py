from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import make_password
from repository.models import User
import hashlib

class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        if email != None and password != None:
            user = None
            hashed_pass = hashing_password(password)
            try:
                user = User.objects.get(email=email, password=hashed_pass)
                print(user)
                return user
            except User.DoesNotExist:
                print("USER NOT FOUND")
                return user
        else :
            print('email not provide')
            return None
    
        
def hashing_password(password):
    hasher = hashlib.sha384(password.encode())
    return hasher.hexdigest()