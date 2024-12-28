from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from blogSite.posts.mixins import PostCreateOrEditMixin
from blogSite.posts.models import Post


# Create your views here.


class PostCreateView(PostCreateOrEditMixin, CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return render(self.request, 'common/success.html', {
            'message': 'Your post has been successfully created!'
        })


class PostEditView(PostCreateOrEditMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return render(self.request, 'common/success.html', {
            'message': 'Your post has been successfully updated!'
        })


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('home')


    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return render(request, 'common/success.html', {
            'message': 'The post has been successfully deleted!'
        })


class PostDetailView(DetailView):
        model = Post
        template_name = 'posts/post-details.html'