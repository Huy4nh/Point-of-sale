# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import uuid

class EmployeeAccountManager(BaseUserManager):
    def create_user(self, staff_id, gmail, username, password=None, **extra_fields):
        if not staff_id:
            raise ValueError('The Staff ID must be set')
        if not gmail:
            raise ValueError('The Email must be set')
        if not username:
            raise ValueError('The Username must be set')
        gmail = self.normalize_email(gmail)
        user = self.model(staff_id=staff_id, gmail=gmail, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_id, gmail, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(staff_id, gmail, username, password, **extra_fields)

class Employee_account(AbstractBaseUser, PermissionsMixin):
    staff_id = models.CharField(max_length=30, primary_key=True)
    gmail = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='employee/', null=True, blank=True)
    username = models.CharField(max_length=40, unique=True,null=False)  # Ensure username is unique
    password = models.CharField(max_length=128)  # Ensure password can store encrypted passwords
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4)
    activation_expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=10))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['staff_id', 'gmail']

    objects = EmployeeAccountManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.gmail.split('@')[0]
        if not self.password:   
            self.password=self.username
        super(Employee_account, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_admin
