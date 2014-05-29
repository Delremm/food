from django.contrib.sites.models import get_current_site
from django.conf import settings


def general_context(request):
    context_extras = {}
    context_extras['current_site'] = get_current_site(request)
    context_extras['default_title'] = settings.SITE_CONTEXT['default_title']
    return context_extras
