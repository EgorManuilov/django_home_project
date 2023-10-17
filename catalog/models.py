from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='media/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateField(auto_now_add=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    # user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    version_current = models.BooleanField(default=True, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.product}, {self.version_number}, {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


