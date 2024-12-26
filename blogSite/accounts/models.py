from django.contrib.auth.models import AbstractUser
from django.db import models
from blogSite.accounts.validators import capitalized_letter, only_letters


# Create your models here.


class AppUser(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[capitalized_letter,
                    only_letters]
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[capitalized_letter,
                    only_letters]
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"