from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse

from flatblocks.models import FlatBlock


class FlatblocksView(View):

    def get(self, request, *args, **kwargs):
        try:
            fb = FlatBlock.objects.get(slug=kwargs.get('slug', None))
        except:
            return HttpResponse('', content_type='text/plain;charset=utf-8')
        return HttpResponse(fb.content, content_type='text/plain;charset=utf-8')
