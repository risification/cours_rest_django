from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from .models import Promocode, Order
from django.utils import timezone


def use_promo(order_id, promocode):
    order = Order.objects.get(id=order_id)
    promo_list = Promocode.objects.filter(status='active', end_date__gt=timezone.now())
    for promo in promo_list:
        if promo.code == promocode:
            order.total_price = order.total_price - order.total_price * promo.sale
    order.save()
    return order.total_price


def get_pay(order_id, total_sum):
    obj = Order.objects.get(id=order_id)
    promo_price = use_promo(order_id, obj.promocode)
    card = obj.user.userprofile.cards.filter(status='default')[0]
    if obj.payment_type == 'card' and obj.status != 'closed':
        try:
            card.balance -= promo_price
            card.save()
            obj.status = 'closed'
            obj.save()
        except IntegrityError:
            raise ValidationError("Not enough money!!!")
    obj.total_price = promo_price
    obj.save()
