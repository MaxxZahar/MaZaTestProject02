from rest_framework import serializers
from ..models import Photo, Album, Tag
from ..settings import ALLOWED_IMAGE_EXTENSIONS, FILE_SIZE_LIMIT
from django.core.validators import FileExtensionValidator
from .tag import TagSerializer


class UserPhotoForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Album.objects.filter(user=self.context.get('request').user)


def validate_file_size(temp_file):
    if temp_file.size > FILE_SIZE_LIMIT * 10 ** 6:
        raise serializers.ValidationError('This image is too large.')
    return temp_file


class PhotoSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS), validate_file_size])
    album = UserPhotoForeignKey()
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Photo
        fields = '__all__'





