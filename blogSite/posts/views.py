from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from blogSite.posts.forms import CommentForm
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

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['comment_form'] = CommentForm()
            context['comments'] = self.object.comments.all()
            context['total_likes'] = self.object.total_likes()
            context['liked'] = self.request.user in self.object.likes.all()
            return context


class PostLikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('post-details', pk=pk)

class CommentCreateView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return redirect('post-details', pk=pk)