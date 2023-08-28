from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='изображение')
    data_create = models.DateField(verbose_name='дата создания')
    sign_publication = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
