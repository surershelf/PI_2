
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set", # Specify the related_name here
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set", # Specify the related_name here
        related_query_name="custom_user",
    )