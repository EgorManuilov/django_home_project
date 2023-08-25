from django.db import models


class Materials(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField()
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='изображение')
    date_creation = models.TimeField(verbose_name=)