from django.urls import path

from . import views

# app_name = "blogs"
urlpatterns = [

    # path("<int:user_id>/", views.IndexView.as_view(), name="index"),

    path("create/", views.BlogCreateView.as_view(), name="blog_create_view"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail_view"),
    path("<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog_update_view"),
    # path("<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="blog_delete_view"),

    path("tag/<int:pk>/", views.BlogTagView.as_view(), name="blog_tag_view"),

    path("<int:blog_id>/comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment_update_view"),
    # path("<int:pk>/comment/create", views.CommentCreateView.as_view(), name="comment_create_view"),
    # path("<int:blog_id>/comment/<int:pk>//update/", views.CommentUpdateView.as_view(), name="comment_update_view"),
    # path("<int:blog_id>/comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete_view"),
]