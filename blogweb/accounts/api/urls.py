from django.urls import path
from . import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("login/", views.LoginAPIView.as_view(), name="login_api"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout_api"),

    path("get/", views.UserList.as_view(), name="user_list_api"),
    path("get/<int:pk>/", views.UserDetail.as_view(), name="user_detail_api"),
    path("delete/<int:pk>/", views.UserDelete.as_view(), name="user_delete_api"),
    path("create/", views.UserCreate.as_view(), name="user_create_api"),
    path("update/<int:pk>/", views.UserUpdate.as_view(), name="user_update_api"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
