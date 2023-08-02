from django.db import models
from extensions.utils import jalali_converter
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, Group

class UserManager(BaseUserManager):
    def create_user(self, name, password, phone, email, **other_fields):
        if not name:
            raise ValueError("نام کاربری یک فیلد اجباری است.")
        if not password:
            raise ValueError("رمز عبور یک فیلد اجباری است")
        if not phone:
            raise ValueError("شماره تلفن یک فیلد اجباری است")
        if not email:
            raise ValueError("ایمیل یک فیلد اجباری است")
        
        user = self.model(name=name, phone=phone, email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password, phone, email, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_second_admin', True)
        other_fields.setdefault('is_third_admin', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        
        return self.create_user(name, password, phone, email, **other_fields)

class User(AbstractBaseUser):
    name = models.CharField(unique=True, max_length=20)
    phone = models.CharField(unique=True, max_length=11)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_second_admin = models.BooleanField(default=True)
    is_third_admin = models.BooleanField(default=False)
    password1 = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150)
    objects = UserManager()
    USERNAME_FIELD = 'name'
    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    REQUIRED_FIELDS = ['phone', 'email']

    def save(self, *args, **kwargs):
        if not self.pk and self.password1 and self.password2:
            # Perform password validation and hashing when creating a new user
            if self.password1 != self.password2:
                raise ValueError("Passwords do not match.")
            self.set_password(self.password1)
        super(User, self).save(*args, **kwargs)

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
