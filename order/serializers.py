from rest_framework import serializers
from .models import Order
from accounts.services import *


class OrderSerializers(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(min_value=0, read_only=True)
    total_sum = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = ['id', 'meal', 'quantity', 'table', 'date_created', 'status', 'total_price', 'total_sum',
                'user']

    def get_total_sum(self, obj):
        total_sum = obj.meal.price * obj.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum

    def get_order_count(self, obj):
        count_orders(obj.user.userprofile)
