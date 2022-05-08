from rest_framework import serializers
from ..models import Photo, Tag
from .tag import TagSerializer


class UpdatePhotoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    # tags = serializers.CharField(max_length=255)

    class Meta:
        model = Photo
        fields = ('title', 'tags')

    def get_or_create_tags(self, tags):
        tag_ids = []
        for tag in tags:
            if Tag.objects.filter(name=tag.get('name')):
                tag_instance = Tag.objects.filter(name=tag.get('name')).get()
            else:
                tag_instance, created = Tag.objects.get_or_create(name=tag.get('name'), defaults=tag)
            tag_ids.append(tag_instance.id)
        return tag_ids

    def create_or_update_tags(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, created = Tag.objects.update_or_create(name=tag.get('name'), defaults=tag)
            tag_ids.append(tag_instance.id)
        print(tag_ids)
        return tag_ids

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        photo = Photo.objects.create(**validated_data)
        photo.tags.set(self.get_or_create_tags(tags))
        return photo

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        print(tags)
        instance.tags.set(self.create_or_update_tags(tags))
        try:
            setattr(instance, 'title', validated_data['title'])
        except KeyError:
            pass
        instance.save()
        return instance


