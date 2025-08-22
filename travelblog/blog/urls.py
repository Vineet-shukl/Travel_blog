# blog/urls.py
from django.urls import path
from .views import home, post_detail, create_post, edit_post, delete_post,register
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:pk>/edit/', edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('register/',register, name='register'),
]