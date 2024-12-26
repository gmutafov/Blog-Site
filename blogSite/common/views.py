
from django.shortcuts import render
from django.views.generic import ListView

from blogSite.posts.models import Post


# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'common/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')

        return queryset


