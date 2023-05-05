from django.urls import path
from .views import *

urlpatterns = [

    path('register/', UserCreate.as_view()),
    path('change_password/<int:pk>/', ChangePasswordView.as_view()),
    path('user_update/<int:pk>/', UpdateUserView.as_view()),
    path('user/all/', UserListView.as_view()),
    path('profile/<int:pk>/', ProfileUpdateView.as_view()),
    path('profile_image/<int:pk>/', ProfileImageUpdateView.as_view()),
    path('profile_video/<int:pk>/', ProfileVideoUpdateView.as_view()),
]
