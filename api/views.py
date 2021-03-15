from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import views, status


# Create your views here.

class MealViewHard(views.APIView):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        serializers = MealSerializersHard(meals, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = MealSerializersHard(data=request.data)
        if serializers.is_valid():
            name = serializers.data.get('name')
            description = serializers.data.get('description')
            price = serializers.data.get('price')
            portion = serializers.data.get('portion')
            Meal.objects.create(name=name, description=description, price=price,
                                portion=portion
                                )
            return Response({"data": "OK"})
        return Response(serializers.errors)


class MealView(views.APIView):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        serializers = MealSerializer(meals, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = MealSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data": "OK"}, status=status.HTTP_201_CREATED)


class MealDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(id=kwargs['meal_id'])
        except Meal.DoesNotExist:
            return Response({"data": "Meal Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializers = MealSerializer(meal)
        return Response(serializers.data)


class CategoryView(views.APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)


class CategoryDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(name=kwargs['category_name'])
        except Category.DoesNotExist:
            return Response({"data": "Category Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializers = CategoryDetailSerializer(category)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = CategoryDetailSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data": "OK"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)
