from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Meal
from .models import Order, MealToOrder
from accounts.services import *
from django.db import IntegrityError
from .services import *


class MTOSerializers(serializers.ModelSerializer):
    class Meta:
        model = MealToOrder
        fields = ['id', 'meal', 'quantity']


class OrderSerializers(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(min_value=0, read_only=True)
    MTO = MTOSerializers(many=True)
    total_sum = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = ['id', 'table', 'date_created', 'status', 'total_price',
                  'user', 'payment_type', 'promocode', 'MTO', 'total_sum']

    def create(self, validated_data):
        mto_data = validated_data.pop('MTO')
        order = Order.objects.create(**validated_data)
        for mto in mto_data:
            MealToOrder.objects.create(order=order, **mto)
        return order

    def get_total_sum(self, obj):
        total_sum = 0
        for mto in obj.MTO.all():
            total_sum = mto.meal.price * mto.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum
