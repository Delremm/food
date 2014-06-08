from django.db import models
from django.contrib.flatpages.models import FlatPage

class ExtendedFlatPage(FlatPage):
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_title = models.TextField(null=True, blank=True)
