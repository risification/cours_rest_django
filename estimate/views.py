from django.shortcuts import render
from .serializers import *
from rest_framework import views, status
from rest_framework.response import Response


# Create your views here.


class RateView(views.APIView):
    def get(self, *args, **kwargs):
        rates = Rate.objects.all()
        serializers = RateSerializers(rates, many=True)
        return Response(serializers.data)
