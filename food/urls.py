from django.conf.urls import patterns, include, url
from django.contrib import admin
from djrill import DjrillAdminSite

admin.site = DjrillAdminSite()
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^apps/macro/', include('macro.urls', namespace="macro")),
    url(r'^api/apps/macro/', include('macro.api.urls', namespace='macro_api')),
    url(r'^emailer/', include('emailer.urls', namespace='emailer')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    (r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^', include('food_app.urls', namespace="apps")),
)

# flatpages
urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^pages/contacts/$', 'flatpage', {'url': '/contacts/'}, name='contacts'),
)

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
