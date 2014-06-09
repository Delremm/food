# coding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin


class Configuration(models.Model):
    """
    Модель настроек сайта
    """

    SECTIONS = (
        ('common', u'Общий'),
        ('texts', u'Тексты'),
        ('external_scripts', u'Внешние скрипты'),
        ('phrases', u'Фразы'), )

    OUTPUT_TYPE = (
        ('string', u'Строка'),
        ('text', u'Текст'),
        ('url', u'Ссылка'),
        ('email', u'Email'),
        ('date', u'Дата'),
        ('checkbox', u'Да/Нет'),
        ('choices', u'Выбор из списка'),
        ('integer', u'Целое'),
        ('float', u'Дробное'),
        ('json', u'JSON'), )

    title = models.CharField(u'Название', max_length=100, )
    name = models.SlugField(
        u'Имя',
        unique=True,
        max_length=100, )
    section = models.CharField(
        u'Раздел',
        choices=SECTIONS,
        max_length=100,
        default='common', )
    output_type = models.CharField(
        u'Тип',
        choices=OUTPUT_TYPE,
        max_length=20,
        blank=False,
        default='string', )
    value = models.CharField(
        u'Значение',
        max_length=6000,
        null=True,
        blank=True, )

    def __unicode__(self):
        """
        Представление объекта в виде unicode-строки
        """
        return self.title

    def get_absolute_url(self):
        return reverse('formeal:configuration', args=[self.name])
