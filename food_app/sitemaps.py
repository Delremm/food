from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 1.6
    changefreq = 'dayly'

    def items(self):
        return ['home', 'macro:tdee']

    def location(self, item):
        return reverse(item)


sitemaps_dict = {
    'static': StaticViewSitemap,
    'flatpages': FlatPageSitemap
}
