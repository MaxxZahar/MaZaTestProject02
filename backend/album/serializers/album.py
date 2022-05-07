from rest_framework import serializers
from ..models import Album, Photo
from .photo import PhotoSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    album_photo = PhotoSerializer(read_only=True, many=True)
    number_of_photos = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'user', 'number_of_photos', 'album_photo', 'created_at')

    def get_id(self, obj):
        return obj.id

    def get_number_of_photos(self, obj):
        queryset = Photo.objects.filter(album=self.get_id(obj))
        return len(queryset)

