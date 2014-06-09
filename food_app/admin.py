# -*- coding:utf-8 -*-

"""
Управление сайтом
"""
from django import forms
from django.contrib import admin
from django.conf import settings
from django.contrib.sites.models import Site

from .models import Configuration


class ConfigurationForm(forms.ModelForm):
    """
    Форма редактирования настроек
    """

    class Meta(object):
        """
        Настройки формы
        """
        widgets = {
            'value': forms.Textarea(
                attrs={'style': 'width:80%'})
        }


class ConfigurationAdmin(admin.ModelAdmin):
    """
    Управление настройками
    """
    search_fields = ('title', 'name', 'value', )
    fields = ('title', 'name', 'section', 'output_type', 'value')
    list_filter = ('section', )
    list_display_links = ('title', )
    form = ConfigurationForm
    list_display = ('title', 'section', 'name', 'value', )


admin.site.register(Configuration, ConfigurationAdmin)
