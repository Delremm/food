# coding: utf-8

from django.conf.urls import *
from food_app.views import FlatblocksView


urlpatterns = patterns(
    '',
    url(
        r'^texts/(?P<slug>\w+)/$',
        FlatblocksView.as_view(), name="texts"),
)
