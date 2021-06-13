from django.db import models


class SuperUser(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=250, null=False, default="")
    email_id = models.EmailField(null=False, default="", unique=True)
    phone = models.CharField(max_length=15, null=False, default="")

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=250, null=False, blank=False, default="")
    phone = models.CharField(max_length=13, null=False, blank=False, default="")
    username = models.CharField(max_length=50,null=False,blank=False,default="")
    password = models.CharField(max_length=250, null=False, blank=False, default="")
    email = models.EmailField(null=True, blank=True)
    aadhaar_card = models.CharField(max_length=12, null=False, blank=False, default="")
    pan_card = models.CharField(max_length=20, null=False, blank=False, default="")
    total_amount = models.FloatField(null=False, blank=False, default=0)
    address = models.TextField(null=False, blank=False, default="")
    area = models.CharField(max_length=100, null=False, blank=False, default="")
    is_active = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PickupMan(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=250, null=False, blank=False, default="")
    phone = models.CharField(max_length=13, null=False, blank=False, default="")
    username = models.CharField(max_length=50,null=False,blank=False,default="")
    password = models.CharField(max_length=250, null=False, blank=False, default="")
    email = models.EmailField(null=True, blank=True)
    aadhaar_card = models.CharField(max_length=12, null=False, blank=False, default="")
    total_amount = models.FloatField(null=False, blank=False, default=0)
    address = models.TextField(null=False, blank=False, default="")
    area = models.CharField(max_length=100, null=False, blank=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return self.user.name
class Otp(models.Model):
    otp = models.IntegerField(null=True)
    otp_time = models.DateTimeField( null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counter = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.user)