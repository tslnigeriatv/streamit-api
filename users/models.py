from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken

# Password Reset
from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
# from django_rest_passwordreset.signals import reset_password_token_created

# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """

#     def create_user(self, email, username, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, username, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, username, password, **extra_fields)


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'twitter': 'twitter', 'email': 'email'}
class CustomUser(AbstractUser):
    # username = None
    # email = models.EmailField(name='email', verbose_name='email', unique=True)
    
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField('email address', unique = True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['username']

    # objects = CustomUserManager()
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def __str__(self):
        return self.email


@receiver(post_save, sender=CustomUser)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



