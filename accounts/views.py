from django.shortcuts import render
from rest_framework import views, status
from .serializers import *
from rest_framework.response import Response
from .services import *

# Create your views here.

class RestaurantProfileView(views.APIView):
    def get(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        serializers = RestaurantProfileSerializers(profile, many=False)
        return Response(serializers.data)

    def put(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        serializers = RestaurantProfileSerializers(profile, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"UPDATE SUCCESSFUL"})
        return Response(serializers.errors)

    def delete(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        profile.delete()
        return Response({"data": "OK"})


class TableView(views.APIView):
    def get(self, request, *args, **kwargs):
        table = Table.objects.all()
        serializers = TableSerializers(table, many=True)
        return Response(serializers.data)


class TableDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            table = Table.objects.get(id=kwargs['table_id'])
        except Table.DoesNotExist:
            return Response({"data": "table Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializers = TableDetailSerializer(table)
        return Response(serializers.data)


class UserProfileView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        serializers = UserProfileSerializers(profile)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        serializers = CardCreateSerializers(data=request.data)
        if serializers.is_valid():
            number = serializers.data.get('number')
            date = serializers.data.get('date')
            holder = serializers.data.get('holder_name')
            code = serializers.data.get('code')
            Card.objects.create(profile=profile, number=number, date=date,
                                holder_name=holder, code=code)
            return Response({"CARD ADDED SUCCESFULLY!"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)
