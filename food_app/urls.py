# coding: utf-8

from django.conf.urls import *
from food_app.views import FlatblocksView, OrderView, CheckoutView


urlpatterns = patterns(
    '',
    # /texts/ is used in macro app in description divs for ajax loading
    url(
        r'^texts/(?P<slug>\w+)/$',
        FlatblocksView.as_view(), name="texts"),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^api/', include('food_app.api_urls', namespace='food_api')),
)
