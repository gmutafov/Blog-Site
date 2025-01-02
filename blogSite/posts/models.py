from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models


UserModel = get_user_model()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    content = models.TextField()
    image = models.URLField(blank=True, null=True, max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    likes = models.ManyToManyField(UserModel, related_name='liked_posts', blank=True)


    def __str__(self):
        return self.title


    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
