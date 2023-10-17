from django.db import models


# Create your models here.
class Blog(models.Model):
    title_post = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    content_post = models.CharField(max_length=3500, verbose_name='Содержание статьи')
    image_post = models.ImageField(upload_to='preview', verbose_name='Изображение', null=True, blank=True)
    data_post = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publ_on_off = models. BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.CharField(max_length=50, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return f'{self.title_post} {self.image_post} {self.data_post}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'