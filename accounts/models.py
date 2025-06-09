from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField

class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    is_active = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username'] 
    def __str__(self):
        return self.username

