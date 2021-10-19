from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):

    def create_user(self, username, email, password):
        # validate email and username
        if not email:
            raise ValueError('Please provide your email address!')

        if not username:
            raise ValueError('Your username is required!')

        # create user
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):

        superuser = self.create_user(
            username=username,
            email=email,
            password=password
        )

        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_admin = True
        superuser.is_superuser = True

        superuser.save(using=self._db)
        return superuser


class Account(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


