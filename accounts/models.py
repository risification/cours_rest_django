from django.contrib.auth.models import User
from django.db import models
from order.models import *


# Create your models here.

class RestaurantProfile(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField()
    salary = models.PositiveIntegerField(default=0)
    schedule = models.CharField(choices=(
        ('2/2', '2/2'),
        ('5/2', '5/2')
    ), max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Table(models.Model):
    area = models.CharField(choices=(
        ('main', 'main'),
        ('vip', 'vip'),
        ('street', 'street')
    ), max_length=50)
    status = models.CharField(choices=(
        ('reserved', 'reserved'),
        ('empty', 'empty')
    ), max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    bonuses = models.PositiveIntegerField(default=0, blank=True)
    order_count = models.PositiveIntegerField(default=0, blank=True)


class Card(models.Model):
    balance = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=(
        ('default', 'default'),
        ('non active', 'non active')
    ), max_length=15, default='non active')
    number = models.IntegerField()
    holder_name = models.CharField(max_length=50)
    date = models.DateField()
    code = models.IntegerField()
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cards')
