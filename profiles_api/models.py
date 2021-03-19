from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) # Create a models

        user.set_password(password) # encrypted/hashed
        user.save(using=self._db) # saving objects in Django

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        user = create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    # Add fields to models
    email = models.EmailField(max_length=255, unique=True)
    name    = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() # Will create it after sometime

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.NAME

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.NAME

    def __str__(self):
        """Return string representation of our user"""
        return self.email
