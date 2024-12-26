from django.urls import path

from blogSite.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]