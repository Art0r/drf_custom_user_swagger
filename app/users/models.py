import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from app.users.managers import UserManager


class Base(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True,
                          default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, blank=True, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, blank=True, null=False)
    is_active = models.BooleanField(
        default=True, editable=True, blank=True, null=False)

    class Meta:
        abstract = True


class UserRoles(models.TextChoices):

    admin = 0
    manager = 1
    employee = 2
    customer = 3


class User(Base, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True, max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    role = models.IntegerField(
        choices=UserRoles.choices, default=3, null=False, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('created_at',)
