from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/images/", blank=True, null=True, default="users/images/default/avatar.jpeg")
    website = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
    
