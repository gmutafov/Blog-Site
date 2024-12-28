from django import forms

from blogSite.posts.models import Post, Comment


class PostsBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'}),
        }