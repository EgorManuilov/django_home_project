from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True,null=True)
    phone = models.CharField(max_length=25, verbose_name='номер телефона', blank=True,null=True)
    country = models.CharField(max_length=15, verbose_name='страна', blank=True,null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

