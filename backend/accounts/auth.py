from accounts.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ValidationError

class Authentication:
    def signin(self, email: str, password: str):
        user = User.objects.filter(email=email).first()
        
        if user and check_password(password, user.password):
            return user
        
        return False
    
    
    def signup(self, name: str, email: str, password: str):
        if User.objects.filter(email=email).exists():
            raise ValidationError("O email já está em uso.")
        
        user = User.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )
        
        return user
