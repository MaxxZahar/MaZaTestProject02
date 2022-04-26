from rest_framework import serializers
from ..models import Album


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Album
        fields = '__all__'
