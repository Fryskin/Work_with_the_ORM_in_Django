from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone_number = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE)
    preview = models.ImageField(upload_to='user/', verbose_name='preview', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
