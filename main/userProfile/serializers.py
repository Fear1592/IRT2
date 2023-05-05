from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, Profile, Images, Videos


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "profile", "image"]


class ProfileVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ["id", "profile", "video"]


class ProfileSerializer(serializers.ModelSerializer):
    images = ProfileImageSerializer(many=True, read_only=True)
    videos = ProfileVideoSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(required=False, allow_empty=True,
                                            child=serializers.ImageField(max_length=1000000, use_url=False),
                                            default=[],
                                            write_only=True
                                            )
    uploaded_videos = serializers.ListField(required=False, allow_empty=True,
                                            child=serializers.FileField(max_length=1000000, use_url=False),
                                            default=[],
                                            write_only=True
                                            )

    class Meta:
        model = Profile
        fields = ['id', 'avatar', 'bio', 'vk', 'inst',
                  'telegram', 'user', 'balance',
                  'is_subscription', 'images', 'uploaded_images',
                  'videos', 'uploaded_videos']
        read_only_fields = ['id', 'user', 'balance', 'is_subscription']

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', None)
        if uploaded_images:
            profile_image_model_instance = [Images(profile=instance, image=image) for image in uploaded_images]
            Images.objects.bulk_create(
                profile_image_model_instance
            )
        uploaded_videos = validated_data.pop('uploaded_videos', None)
        if uploaded_videos:
            profile_video_model_instance = [Videos(profile=instance, video=video) for video in uploaded_videos]
            Videos.objects.bulk_create(
                profile_video_model_instance
            )
        return super().update(instance, validated_data)


class ProfileManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'vk', 'inst', 'telegram', 'user', 'balance', 'is_subscription', 'images',
                  'uploaded_images']
        read_only_fields = ['avatar', 'bio', 'vk', 'inst', 'telegram', 'user', ]


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'password2', 'username',
                  'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совспадают"})

        return attrs

    def create(self, validated_data):
        user = UserProfile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        profile = Profile.objects.create(
            user=user
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Старый пароль не верный"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "Нету прав"})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if UserProfile.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "Такая почта уже используется"})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if UserProfile.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "Такое имя уже используется"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "Нету прав"})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
