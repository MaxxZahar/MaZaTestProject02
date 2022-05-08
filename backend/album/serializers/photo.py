from rest_framework import serializers
from ..models import Photo, Album
from ..settings import ALLOWED_IMAGE_EXTENSIONS
from django.core.validators import FileExtensionValidator


class UserPhotoForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Album.objects.filter(user=self.context.get('request').user)


class PhotoSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])
    album = UserPhotoForeignKey()

    class Meta:
        model = Photo
        fields = '__all__'
