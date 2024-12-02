from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.

class User(AbstractUser, PermissionsMixin):

    TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('employee', 'Employee')
    )


    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    type_user = models.CharField(choices=TYPE_CHOICES, max_length=255, default='user')
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'password']

    def __str__(self):
        return self.email