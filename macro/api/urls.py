from django.conf.urls import patterns, url, include
from rest_framework import routers

from macro.api import views

urlpatterns = patterns(
    '',
    url(
        r'^tdee/$',
        views.MacroDataView.as_view(), name="tdee"),
)
