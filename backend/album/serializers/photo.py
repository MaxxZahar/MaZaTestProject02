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


def calculate_small_size(width, height):
    if width <= 150 and height <= 150:
        return {
            'small_width': width,
            'small_height': width
        }
    if height > width:
        return {
            'small_width': round(150 * width / height),
            'small_height': 150
        }
    if width >= height:
        return {
            'small_width': 150,
            'small_height': round(150 * height / width)
        }


class PhotoSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(validators=[FileExtensionValidator(ALLOWED_IMAGE_EXTENSIONS), validate_file_size])
    album = UserPhotoForeignKey()
    tags = TagSerializer(many=True, required=False)
    small_height = serializers.SerializerMethodField()
    small_width = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_small_height(self, obj):
        return calculate_small_size(obj.img_width, obj.img_height)['small_height']

    def get_small_width(self, obj):
        return calculate_small_size(obj.img_width, obj.img_height)['small_width']

    def get_or_create_tags(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, created = Tag.objects.get_or_create(name=tag.get('name'), defaults=tag)
            tag_ids.append(tag_instance.id)
            print(tag_ids, 'goc')
        return tag_ids

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        print(tags, 'c')
        photo = Photo.objects.create(**validated_data)
        photo.tags.set(self.get_or_create_tags(tags))
        return photo






