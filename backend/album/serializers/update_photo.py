from rest_framework import serializers
from ..models import Photo


class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title',)
