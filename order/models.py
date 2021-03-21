from accounts.models import *
from django.contrib.auth.models import User
from django.db import models
from api.models import *


# Create your models here.

class Order(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=(
        ('ready', 'ready'),
        ('in_process', 'in_process')
    ), max_length=20, default='in_process')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
