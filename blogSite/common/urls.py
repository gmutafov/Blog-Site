from django.urls import path

from blogSite.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutUsPageView.as_view(), name='about'),
    path('failure/', views.Failure.as_view(), name='failure'),

]