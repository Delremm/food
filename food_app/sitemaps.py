from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'macro:tdee']

    def location(self, item):
        return reverse(item)


sitemaps_dict = {
    'static': StaticViewSitemap,
    'flatpages': FlatPageSitemap
}
