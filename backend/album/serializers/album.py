from rest_framework import serializers
from ..models import Album, Photo
from .photo import PhotoSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    album_photo = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Album
        fields = ('name', 'user', 'album_photo', 'created_at')

