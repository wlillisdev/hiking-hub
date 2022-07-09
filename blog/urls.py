from . import views
from .views import AddPostView
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.PostList.as_view(), name="posts"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
