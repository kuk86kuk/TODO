from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=128, null=True)
    
    
    email = models.EmailField(unique=True, null=True)
    
