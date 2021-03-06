"""urls.py"""
from . import views
from .views import AddPostView, PostUpdateView, DeletePostView
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.PostList.as_view(), name="posts"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='update_post'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
