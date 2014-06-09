from django.shortcuts import get_object_or_404
from django.views.generic import View
from formeal_app.models import Configuration
from django.http import HttpResponse

from flatblocks.models import FlatBlock


class ConfigurationView(View):

    def get(self, request, *args, **kwargs):
        conf = get_object_or_404(Configuration, name=kwargs.get('slug', None))
        return HttpResponse(conf.value, content_type='text/plain;charset=utf-8')
