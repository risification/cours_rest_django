from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .serializers import *


# Create your views here.


class OrderView(views.APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializers = OrderSerializers(orders, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = OrderSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data": "OK"})
        return Response(serializers.errors)