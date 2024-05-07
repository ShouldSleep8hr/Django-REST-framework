from django.urls import path
from . import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.UserListView.as_view(), name='user_list_view'),
    path("<int:pk>/", views.UserDetailView.as_view(), name='user_detail_view'),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete_view"),

    #path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name='login'),
    path("<int:pk>/edit/", views.UserUpdateView.as_view(), name="user_update_view"),

    # path("", views.user_list, name='user_list_api'),
    # path("<int:pk>/", views.user_detail, name='user_detail_api'),
    # path("<int:pk>/delete/", views.user_delete, name="user_delete_api"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
