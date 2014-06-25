from django.conf.urls import patterns, url, include
from rest_framework import routers

from food_app.api import AddToCartView

urlpatterns = patterns(
    '',
    url(
        r'^add_to_cart/$',
        AddToCartView.as_view(), name="add_to_cart"),
)
