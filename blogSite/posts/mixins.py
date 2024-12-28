from django.contrib import messages
from django.urls import reverse_lazy

from blogSite.posts.forms import PostsBaseForm
from blogSite.posts.models import Post


class PostCreateOrEditMixin():
    model = Post
    form_class = PostsBaseForm
    template_name = 'posts/post-forms.html'
    success_url = reverse_lazy('home')

