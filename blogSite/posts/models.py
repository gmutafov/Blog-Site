from django.core.validators import MinLengthValidator
from django.db import models

from blogSite.accounts.models import AppUser


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title