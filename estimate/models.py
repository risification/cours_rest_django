from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Rate(models.Model):
    worker = models.CharField(max_length=50)
    star = models.PositiveIntegerField(default=0)
    date_created = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
