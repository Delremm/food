import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView

from flatblocks.models import FlatBlock

from food_app.models import Menu, Dish


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


class OrderView(TemplateView):
    template_name = 'food_app/order.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        # context['menus_breakfast'] = Menu.objects.filter(
        #     date=tomorrow, menu_type=Menu.BREAKFAST)
        # context['menus_lunch'] = Menu.objects.filter(
        #     date=tomorrow, menu_type=Menu.LUNCH)
        # context['menus_dinner'] = Menu.objects.filter(
        #     date=tomorrow, menu_type=Menu.DINNER)
        # context['menus_other'] = Menu.objects.filter(
        #     date=tomorrow, menu_type=Menu.OTHER)
        context['menus'] = [
            [
                Menu.objects.filter(
                    date=tomorrow,
                    menu_type=menu_type[0]),
                menu_type[1]] for menu_type in Menu.MENU_TYPE]
        response = self.render_to_response(context)
        return response
