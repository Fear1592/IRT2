from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, ChangePasswordSerializer, \
    UpdateUserSerializer, UserListSerializer, ProfileSerializer, \
    ProfileImageSerializer, ProfileVideoSerializer
from .models import UserProfile, Profile, Images, Videos


class UserCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateUserSerializer


class UserListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.request.user.id)


class ProfileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        data = request.data
        profile = self.get_object()
        profile.vk = data.get('vk')
        profile.bio = data.get('bio')
        profile.inst = data.get('inst')
        profile.telegram = data.get('telegram')
        if data.get('avatar') != None and data.get('avatar') != '':
            profile.avatar = data.get('avatar')
        profile.save()
        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileImageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ProfileImageSerializer


class ProfileVideoUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = ProfileVideoSerializer
