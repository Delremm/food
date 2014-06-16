from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView

from flatblocks.models import FlatBlock


class FlatblocksView(View):

    def get(self, request, *args, **kwargs):
        try:
            fb = FlatBlock.objects.get(slug=kwargs.get('slug', None))
        except:
            return HttpResponse('', content_type='text/plain;charset=utf-8')
        return HttpResponse(fb.content, content_type='text/plain;charset=utf-8')



class TextFileView(TemplateView):
    """
    A ``TemplateView`` that sets the proper headers
    """
    content_type = 'text/plain'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = self.content_type
        context['ROOT_URL'] = self.request.build_absolute_uri('/')
        return super(TextFileView, self).render_to_response(context, **response_kwargs)
