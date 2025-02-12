from django.contrib import admin
from unfold.admin import ModelAdmin

from blogSite.posts.models import Post


# Register your models here.

@admin.register(Post)
class PostAdminClass(ModelAdmin):
    list_display = ['title', 'content', 'image']