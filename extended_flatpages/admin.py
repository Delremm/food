from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from extended_flatpages.models import ExtendedFlatPage

class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': (
            'url',
            'title',
            'content',
            'sites', 'meta_title', 'meta_keywords', 'meta_description')}),
    )     

#admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)
