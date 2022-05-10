from rest_framework import serializers
from .models import User
from album.models import Album


class UserSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = User
        fields = '__all__'
        fields += 'albums'
        fields += 'user'
