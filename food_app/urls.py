# coding: utf-8

from django.conf.urls import *
from formeal_app.views import ConfigurationView


urlpatterns = patterns(
    '',
    url(
        r'^configuration/(?P<slug>\w+)/$',
        ConfigurationView.as_view(), name="configuration"),
)
