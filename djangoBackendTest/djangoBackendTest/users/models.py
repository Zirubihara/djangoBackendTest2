from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager
from .validators import validate_anulujkredyr_email

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True, validators=[validate_anulujkredyr_email])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    perm = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

