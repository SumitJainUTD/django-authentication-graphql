from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

#class CustomAccountManager(BaseUserManager):
#
#    def create_superuser(self, email, user_name, first_name, password, **other_fields):
#
#        other_fields.setdefault('is_staff', True)
#        other_fields.setdefault('is_superuser', True)
#        other_fields.setdefault('is_active', True)
#
#        if other_fields.get('is_staff') is not True:
#            raise ValueError(
#                'Superuser must be assigned to is_staff=True.')
#        if other_fields.get('is_superuser') is not True:
#            raise ValueError(
#                'Superuser must be assigned to is_superuser=True.')
#
#        return self.create_user(email, user_name, first_name, password, **other_fields)
#
#    def create_user(self, email, user_name, first_name, password, **other_fields):
#
#        if not email:
#            raise ValueError(_('You must provide an email address'))
#
#        email = self.normalize_email(email)
#        user = self.model(email=email, user_name=user_name,
#                          first_name=first_name, **other_fields)
#        user.set_password(password)
#        user.save()
#        return user
#

class NewUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.username
