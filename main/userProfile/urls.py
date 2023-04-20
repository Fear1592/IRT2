from django.urls import path
from .views import *

urlpatterns = [

    path('register/', UserCreate.as_view()),
    path('change_password/<int:pk>/', ChangePasswordView.as_view()),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view()),
    path('user/all/', UserListView.as_view()),
]
