from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('librarian', 'Librarian')])
    groups = models.ManyToManyField(Group, related_name='libraryapp_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='libraryapp_user_permissions', blank=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
