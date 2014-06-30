from django.conf.urls import patterns, url, include
from rest_framework import routers

from food_app.api import AddToCartView, MenusView, MenusByTypeView, OrderOptionsView, CartView,\
    ClearCartView

urlpatterns = patterns(
    '',
    url(
        r'^add_to_cart/$',
        AddToCartView.as_view(), name="add_to_cart"),
    url(
        r'^menu/$',
        MenusView.as_view(), name="menu"),
    url(
        r'^menu_by_type/$',
        MenusByTypeView.as_view(), name="menu_by_type"),
    url(
        r'^order_options/$', OrderOptionsView.as_view(), name="order_options"),
    url(
        r'^cart/$', CartView.as_view(), name="cart"),
    url(
        r'^clear_cart/$', ClearCartView.as_view(), name="clear_cart"),
)
