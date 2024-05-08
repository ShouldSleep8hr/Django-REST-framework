from django.urls import path

from . import views

urlpatterns = [
    path("tag/", views.TagListAPI.as_view(), name="tag_list_api"),
    path("tag/create/", views.TagCreateAPI.as_view(), name="tag_create_api"),
    path("tag/<int:pk>/update/", views.TagUpdateAPI.as_view(), name="tag_update_api"),
    path("tag/<int:pk>/delete/", views.TagDeleteAPI.as_view(), name="tag_delete_api"),

    path("tag/<int:pk>/", views.BlogTagAPI.as_view(), name="blog_tag_api"),

    path("get/", views.BlogListAPI.as_view(), name="blog_list_api"),
    path("get/<int:pk>/", views.BlogDetailAPI.as_view(), name="blog_detail_api"),
    path("create/", views.BlogCreateAPI.as_view(), name="blog_create_api"),
    path("<int:pk>/update/", views.BlogUpdateAPI.as_view(), name="blog_update_api"),
    path("<int:pk>/delete/", views.BlogDeleteAPI.as_view(), name="blog_delete_api"),

    path("get/<int:pk>/comment/", views.CommentListAPI.as_view(), name="comment_list_api"),
    path("<int:pk>/comment/create/", views.CommentCreateAPI.as_view(), name="comment_create_api"),
    path("<int:blog_id>/comment/<int:pk>/update/", views.CommentUpdateAPI.as_view(), name="comment_update_api"),
    path("<int:blog_id>/comment/<int:pk>/delete/", views.CommentDeleteAPI.as_view(), name="comment_delete_api"),
]