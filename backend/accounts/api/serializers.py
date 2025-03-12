from rest_framework import serializers
from django.conf import settings
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','avatar', 'email','name', 'last_login']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['avatar'] =  f'{settings.CURRENT_URL}{instance.avatar}'