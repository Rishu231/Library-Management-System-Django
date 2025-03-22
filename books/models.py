from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Avoid conflict with auth.User by setting unique related names
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="books_users",  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="books_users_permissions",  # Unique related name
        blank=True
    )


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title