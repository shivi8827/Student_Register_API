from django.db import models

from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _




class CustomUserManager(BaseUserManager):
    def normalize_phone(self, phone):
        """
        Normalize the phone number by removing spaces, dashes, etc.
        You can customize this method according to your needs.
        """
        return phone.replace(" ", "").replace("-", "")
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not phone:
            raise ValueError('The given email must be set')
        phone = self.normalize_phone(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)



class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name
    



   #shivi44@11

class CustomUser(AbstractUser):
    username = None
    
    phone = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField(null=True)
    status = models.BooleanField(null=True)
    image = models.ImageField(upload_to='images/')
   # is_active = models.BooleanField(default=False)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()