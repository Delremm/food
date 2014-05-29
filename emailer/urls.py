from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from emailer.views import CreateSubscriberApi

urlpatterns = patterns(
    '',
    url(r'^subscribe/$', CreateSubscriberApi.as_view(), name='subscribe'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
