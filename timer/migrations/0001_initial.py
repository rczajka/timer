# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timer'
        db.create_table('timer_timer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, blank=True)),
            ('change_stamp', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('seconds', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('timer', ['Timer'])


    def backwards(self, orm):
        # Deleting model 'Timer'
        db.delete_table('timer_timer')


    models = {
        'timer.timer': {
            'Meta': {'object_name': 'Timer'},
            'change_stamp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'seconds': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['timer']