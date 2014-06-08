from django.conf.urls import patterns, include, url

from django.contrib import admin
from djrill import DjrillAdminSite

admin.site = DjrillAdminSite()
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^emailer/', include('emailer.urls', namespace='emailer')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    (r'^pages/', include('django.contrib.flatpages.urls')),
)

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
