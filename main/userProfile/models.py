from django.db import models

from django.db import models


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """ Create a new superuser profile """
        user = self.create_user(email, username, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="Почта")
    username = models.CharField(max_length=30, verbose_name="Ник")
    is_staff = models.BooleanField(default=False, verbose_name="Модератор")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    is_superuser = models.BooleanField(default=False, verbose_name="Супер пользователь")
    is_service = models.BooleanField(default=False, verbose_name="Услуги")
    is_maker = models.BooleanField(default=False, verbose_name="Производитель")
    is_shop = models.BooleanField(default=False, verbose_name="Онлайн магазин")
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField('Имя', max_length=30,  blank=True, null=True)
    last_name = models.CharField('Фамилия',max_length=30,  blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        ordering = ['id']
        verbose_name = "Аккаунт пользователя"
        verbose_name_plural = "Аккаунты пользователей"

    def __str__(self):
        return self.email