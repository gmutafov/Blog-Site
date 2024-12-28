from django import forms

from blogSite.posts.models import Post


class PostsBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image',]


