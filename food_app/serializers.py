from rest_framework import serializers
from food_app.models import Menu, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
