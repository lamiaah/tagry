from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token




class CustomAuth(BaseUserManager):

    def _create_user(self, email,  password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff, 
            is_active=True,
            # is_archive =False,  
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email,  password, **extra_fields):
        return self._create_user(email,  password, False, False, **extra_fields)

    def create_superuser(self, email,  password, **extra_fields):
        user=self._create_user(email,  password, True, True, **extra_fields)
        return user

            



class CustomUser(AbstractUser):
    email = models.EmailField(max_length= 50, null= False, blank= False,unique= True)
    # is_archive = models.BooleanField(null=False,blank= False, default= False)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomAuth()


    def __str__(self):
        return self.email

    def get_absolute_url(self):
         return "/users/%i/" % (self.pk)

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender,created=False , instance = None , **kwargs):
    if created:
        Token.objects.create(user=instance)



