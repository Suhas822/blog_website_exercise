from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts_view, name='post_list'),
]
