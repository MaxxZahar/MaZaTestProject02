from rest_framework import serializers
from ..models import Photo
from .tag import TagSerializer


class UpdatePhotoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Photo
        fields = ('title', 'tags')
