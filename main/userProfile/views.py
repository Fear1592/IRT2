from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, ChangePasswordSerializer, \
    UpdateUserSerializer, UserListSerializer
from .models import UserProfile


class UserCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)


class UpdateProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateUserSerializer


class UserListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.request.user.id)
