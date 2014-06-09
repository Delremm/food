# coding: utf-8

from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(
        r'^$',
        TemplateView.as_view(template_name='macro/tdee.html'), name="tdee"),
)
