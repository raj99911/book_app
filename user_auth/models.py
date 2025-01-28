
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('You must set is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('You must set is_superuser = True')
        return self.create_user(email, password, **extra_fields)


USER_ROLE = [
    ('admin', 'ADMIN'),
    ('nrml_user', 'NORMAL USER'),
]


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=30)
    role = models.CharField(choices=USER_ROLE, blank=True, null=True, max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    fullname = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)