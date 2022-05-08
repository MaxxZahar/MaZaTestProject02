from django.db import models
from django.utils import timezone
from .album import Album
from .tag import Tag


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Описание фотографии')
    img = models.ImageField(verbose_name='Фотография')
    tags = models.ManyToManyField(Tag, blank=True, related_name='photo_tag', verbose_name='Список тегов')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_photo', verbose_name='Альбом')
    added_at = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('-added_at',)