from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
