from django.urls import path, re_path
from .views import HomeView, PostDetailView, \
   AddPostView, UpdatePostView, DeletePostView, AddTagView, \
   TagView, UpdateTagView, TagListView, LikeView

urlpatterns = [
   path("", HomeView.as_view(), name="home"),
   path("blog/<int:pk>", PostDetailView.as_view(), name="blog-detail"),
   path("add-post/", AddPostView.as_view(), name="add-post"),
   path("blog/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
   path("blog/<int:pk>/remove", DeletePostView.as_view(), name="delete-post"),
   path("add-tag/", AddTagView.as_view(), name="add-tag"),
   path("edit-tag/<int:pk>/edit", UpdateTagView.as_view(), name="edit-tag"),
   path("tag/<str:tags>", TagView, name="tag"),
   path("tag-list/", TagListView, name="tag-list"),
   path("like/<int:pk>", LikeView, name="like_post"),
]
