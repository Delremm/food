from rest_framework import serializers
from food_app.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
