from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group, Permission
from django.utils import timezone
from .company import Company
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='users', verbose_name="Company")
    username = models.CharField(max_length=150, unique=True, verbose_name="Username")
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Date Joined")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    groups = models.ManyToManyField(
            Group,
            related_name='custom_user_set', 
            blank=True
        )
        
    user_permissions = models.ManyToManyField(
            Permission,
            related_name='custom_user_permissions', 
            blank=True
        )
