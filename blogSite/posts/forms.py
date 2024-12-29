from django import forms

from blogSite.posts.models import Post, Comment


class PostsBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter a Title',
            'class': 'form-control'
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Enter your content',
            'class': 'form-control'
        })
        self.fields['image'].widget.attrs.update({
            'placeholder': 'Add an URL image (optional)',
            'class': 'form-control'
        })

        self.fields['title'].help_text = None
        self.fields['content'].help_text = None
        self.fields['image'].help_text = None

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'}),
        }