# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table(u'formeal_app_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('section', self.gf('django.db.models.fields.CharField')(default='common', max_length=100)),
            ('output_type', self.gf('django.db.models.fields.CharField')(default='string', max_length=20)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=6000, null=True, blank=True)),
        ))
        db.send_create_signal(u'formeal_app', ['Configuration'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table(u'formeal_app_configuration')


    models = {
        u'formeal_app.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'output_type': ('django.db.models.fields.CharField', [], {'default': "'string'", 'max_length': '20'}),
            'section': ('django.db.models.fields.CharField', [], {'default': "'common'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['formeal_app']