from django.db import models
from extensions.utils import jalali_converter
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, Group

# Create your models here.


class UserManager(BaseUserManager):
    def craete_user(self, name, password, phone, email, **other_fields):
        if not name:
            raise ValueError("نام کاربری یک فیلد اجباری است.")
        if not password:
            raise ValueError("رمز عبور یک فیلد اجباری است")
        if not phone:
            raise ValueError("شماره تلفن یک فیلد اجباری است")
        if not email:
            raise ValueError("ایمیل یک فیلد اجباری است")
        
        user = self.model(password=password ,phone=phone, name=name, email=email,
                           **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **other_fields):
        user = self.craete_user(password=password, **other_fields)
        user.is_admin = True
        user.is_second_admin = True
        user.is_third_admin = False
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(unique=True, max_length=20)
    phone = models.CharField(unique=True, max_length=11)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_second_admin = models.BooleanField(default=True)
    is_third_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'name'
    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.name

    def jlast_login(self):
        return jalali_converter(self.last_login)

    def jcreated(self):
        return jalali_converter(self.date_created)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
