from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from blogSite.accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from blogSite.accounts.models import AppUser


# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "registration/login.html"
    context_object_name = 'login'

    def form_invalid(self, form):
        messages.error(self.request, "The username or password is incorrect.")
        return super().form_invalid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = 'profile/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return self.request.user
        raise Http404("No User found")


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = AppUser
    form_class = CustomUserChangeForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDeleteView(DeleteView):
    model = AppUser
    template_name = 'profile/profile-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        logout(request)
        return HttpResponseRedirect(self.success_url)