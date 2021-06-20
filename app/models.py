from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import uuid


def generate_uuid(length: int = 10):
    uid: str = uuid.uuid4().hex
    return uid[0:length]


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Not a valid username")
        user_name = self.normalize_email(username)
        user = self.model(username=user_name, **kwargs)
        user.set_password(password)
        user.user_key = generate_uuid()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have IsSuperuser=True.')

        return self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    user_key = models.CharField(max_length=10, unique=True, default=generate_uuid(10))
    name = models.CharField(max_length=250, null=False, blank=False, default="")
    username = models.CharField(max_length=100, null=False, blank=True, default="", unique=True)
    phone = models.CharField(max_length=10, null=False, blank=False, default="")
    email = models.EmailField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False, null=False, blank=False)
    is_pickupman = models.BooleanField(default=False, null=False, blank=False)
    is_normaluser = models.BooleanField(default=False, null=False, blank=False)
    is_active = models.BooleanField(default=False, null=False, blank=False)
    is_staff = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects: UserManager = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["name", "phone"]

    def save(self, *args, **kwargs):
        self.UserKey = generate_uuid(10)
        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = self.name
        return full_name

    def get_username(self):
        return self.username

    def get_mobile(self):
        return self.phone

    def set_random_password(self):
        password = UserManager().make_random_password()
        self.set_password(password)
        return password

    def __str__(self):
        return self.username


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="")
    aadhaar_card = models.CharField(max_length=12, null=False, blank=False, default="")
    pan_card = models.CharField(max_length=20, null=False, blank=False, default="")
    account_no = models.TextField(null=False, blank=False, unique=True, default=0,max_length='100')
    total_amount = models.FloatField(null=False, blank=False, default=0)
    address = models.TextField(null=False, blank=False, default="")
    area = models.CharField(max_length=100, null=False, blank=False, default="")
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)


class PickupMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="")
    aadhaar_card = models.CharField(max_length=12, null=False, blank=False, default="")
    total_amount = models.FloatField(null=False, blank=False, default=0)
    address = models.TextField(null=False, blank=False, default="")
    area = models.CharField(max_length=100, null=False, blank=False, default="")
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    pickup_man = models.ForeignKey(PickupMan, on_delete=models.CASCADE)
    Transaction_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),

    ]
    transaction_type = models.CharField(max_length=250, choices=Transaction_CHOICES, null=False, blank=False, default="")
    transaction_amount = models.FloatField(null=False, blank=False, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user.name


class Otp(models.Model):
    otp = models.IntegerField(null=True)
    otp_time = models.DateTimeField( null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counter = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)

class Amount(models.Model):
    total_amount= models.BigIntegerField(null=True)