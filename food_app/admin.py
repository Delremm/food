# -*- coding:utf-8 -*-

"""
Управление сайтом
"""
from django import forms
from django.contrib import admin
from django.conf import settings
from django.contrib.sites.models import Site

from food_app.models import Recipe, Dish, Menu

admin.site.register(Recipe)
admin.site.register(Dish)
admin.site.register(Menu)
