from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Table, RestaurantProfile, Card, UserProfile])
