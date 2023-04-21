from datetime import timedelta
import redis
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer
from django.middleware import csrf
import jwt


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

        response = super().post(request, *args, **kwargs)
        refresh_token = request.data.get('refresh')

        decode = jwt.decode(refresh_token, key=settings.SECRET_KEY, algorithms=["HS256"])

        if refresh_token:
            user_id = decode['user_id']
            if user_id:
                access_token = response.data.get('access')
                redis_client.set(f'access_token_{user_id}', access_token, ex=timedelta(minutes=30))

        response.data.pop('refresh', None)

        return response


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

        response = super().post(request, *args, **kwargs)
        access_token = response.data.get('access')
        refresh_token = response.data.get('refresh')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                # Save tokens to Redis
                redis_client.set(f'access_token_{user.id}', access_token, ex=timedelta(minutes=30))
                redis_client.set(f'refresh_token_{user.id}', refresh_token, ex=timedelta(days=14))

                # Set refresh token as HttpOnly cookie
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh_token),
                    httponly=True,
                    max_age=3600 * 24 * 14,  # 14 days
                    domain='127.0.0.1',
                    path='/',
                    secure=False,
                    samesite='None',
                    expires=timedelta(days=14)
                )
                csrf.get_token(request)

                return response
