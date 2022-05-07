from rest_framework import serializers
from user.models import User
from django.contrib.auth import login, authenticate


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

