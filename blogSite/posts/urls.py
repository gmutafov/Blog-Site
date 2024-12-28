from django.urls import path, include

from blogSite.posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', include([
        path('details/', views.PostDetailView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('delete/', views.PostDeleteView.as_view(), name='post-delete'),
    ])),
]