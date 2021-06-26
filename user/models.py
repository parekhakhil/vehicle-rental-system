from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, name, mobile, email, password=None, confirm_password=None):
        if not mobile:
            return ValueError("Please enter your 10 digit mobile no.")

        if not name:
            return ValueError("Please provide your name")

        if not email:
            return ValueError("Please provide your email")

        if len(password) < 8:
            return ValueError("Password must contain 8 characters")

        if password != confirm_password:
            return ValueError("Confirm password must match")

        userObj = self.model(name=name, mobile=mobile, email=email)
        userObj.set_password(password)
        userObj.save(using=self._db)
        return userObj

    def create_staffuser(self, name, email, mobile, password=None):
        if not mobile:
            return ValueError("Please enter your 10 digit mobile no.")

        if not email:
            return ValueError("Please provide your email")

        if not name:
            return ValueError("Please provide ypur name")

        userObj = self.model(name=name, email=email, mobile=mobile)
        userObj.set_password(password)
        userObj.save(using=self._db)
        return userObj

    def create_superuser(self, name, mobile, password=None):
        if not mobile:
            return ValueError("Please enter your 10 digit mobile no.")

        if not name:
            return ValueError("Please provide ypur name")

        userObj = self.model(name=name, mobile=mobile, admin=True)
        userObj.set_password(password)
        userObj.save(using=self._db)
        return userObj


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    mobile = models.CharField(max_length=10, unique=True)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.mobile

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return True

    @property
    def is_staff(self):
        return True

    objects = CustomUserManager()
