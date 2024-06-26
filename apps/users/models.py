from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/images/",
        blank=True,
        null=True,
        default="users/images/default/avatar.jpeg",
    )
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.username
