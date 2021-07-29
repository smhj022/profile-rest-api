from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an Email Address")

        # it will lowercase the second half of the email after @ e.g. @gmail.com
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # with set_password django will save password as a hash password
        user.set_password(password)

        # standard procedure for saving the objects
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user using details"""
        user = self.create_user(email, name, password)

        # is_superuser is automatically created by mixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom model manager for the user model : It knows how to create user and
    # control user using django command line

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve full name of user"""
        return self.name

    def __str__(self) -> str:
        """return string representation of our user"""
        return self.email
