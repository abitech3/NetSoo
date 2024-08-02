from django.db import models
from django.contrib.auth.models import AbstractUser 
from PIL import Image
from .managers import UserManager 



# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        null=True,
        blank=True,
    )

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []







    