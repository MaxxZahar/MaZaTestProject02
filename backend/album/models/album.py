from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_album', verbose_name='Владелец')
    created_at = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('-created_at',)