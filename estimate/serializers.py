from .models import *
from rest_framework import serializers


class RateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
