from rest_framework import serializers
from ..models import Photo
from ..settings import ALLOWED_IMAGE_EXTENSIONS
from django.core.validators import FileExtensionValidator


class PhotoSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS)])

    class Meta:
        model = Photo
        fields = '__all__'
