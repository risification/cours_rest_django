from rest_framework import serializers
from .models import *
from order.serializers import OrderSerializers
from order.models import *


class RestaurantProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = RestaurantProfile
        fields = '__all__'


class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableDetailSerializer(serializers.ModelSerializer):
    order_set = OrderSerializers(many=True)

    class Meta:
        model = Table
        fields = ['id', 'area', 'status', 'order_set']


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardCreateSerializers(serializers.Serializer):
    number = serializers.IntegerField()
    date = serializers.DateField()
    holder_name = serializers.CharField(max_length=20)
    code = serializers.IntegerField(min_value=100, max_value=999)


class UserProfileSerializers(serializers.ModelSerializer):
    cards = CardSerializers(many=True)
    bonuses = serializers.IntegerField(read_only=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'street', 'house', 'address', 'bonuses', 'order_count', 'email', 'cards']
