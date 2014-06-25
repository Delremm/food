# coding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin

from filer.fields.image import FilerImageField


class Recipe(models.Model):
    image = FilerImageField()
    text = models.TextField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    SALAD = 'SA'
    SOUP = 'SO'
    SECOND = "SE"
    OTHER = 'OT'
    DISH_TYPE = (
        (SALAD, 'Салат'),
        (SOUP, 'Суп'),
        (SECOND, 'Второе'),
        (OTHER, 'Другое'),
    )
    title = models.CharField(max_length=255)
    dish_type = models.CharField(max_length=2, choices=DISH_TYPE, default=OTHER)
    description = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey('Recipe', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    LUNCH = 'LU'
    DINNER = 'DI'
    BREAKFAST = 'BR'
    OTHER = 'OT'
    MENU_TYPE = (
        (LUNCH, 'Обед'),
        (DINNER, 'Ужин'),
        (BREAKFAST, 'Завтрак'),
        (OTHER, 'Другое'),
    )
    date = models.DateField()
    menu_type = models.CharField(
        max_length=2, choices=MENU_TYPE, default=LUNCH)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return str(self.date)
