from django.db import models
from django.contrib.auth.models import AbstractUser

from .user_manager import UserManager


class User(AbstractUser):
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    GENDER = (("male", "male"), ("female", "female"), ("other", "other"))

    username = None
    date_joined = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER)
    birthdate = models.DateField()
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    profile_picture = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
