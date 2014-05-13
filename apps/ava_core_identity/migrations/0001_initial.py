# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Identity'
        db.create_table(u'ava_core_identity_identity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'ava_core_identity', ['Identity'])


    def backwards(self, orm):
        # Deleting model 'Identity'
        db.delete_table(u'ava_core_identity_identity')


    models = {
        u'ava_core_identity.identity': {
            'Meta': {'object_name': 'Identity'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['ava_core_identity']