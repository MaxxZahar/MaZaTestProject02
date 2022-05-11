from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    is_active = serializers.HiddenField(default=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_active')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            email=validated_data['email'],
            is_active=validated_data['is_active'],)
        user.save()
        return user
