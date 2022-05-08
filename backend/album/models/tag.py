from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя тега')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
