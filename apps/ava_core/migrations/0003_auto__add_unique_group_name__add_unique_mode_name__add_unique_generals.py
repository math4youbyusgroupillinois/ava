# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Group', fields ['name']
        db.create_unique(u'ava_core_group', ['name'])

        # Adding unique constraint on 'Mode', fields ['name']
        db.create_unique(u'ava_core_mode', ['name'])

        # Adding unique constraint on 'GeneralStatus', fields ['name']
        db.create_unique(u'ava_core_generalstatus', ['name'])

        # Adding unique constraint on 'UserPreference', fields ['name']
        db.create_unique(u'ava_core_userpreference', ['name'])

        # Adding unique constraint on 'Module', fields ['name']
        db.create_unique(u'ava_core_module', ['name'])

        # Adding unique constraint on 'UserStatus', fields ['name']
        db.create_unique(u'ava_core_userstatus', ['name'])

        # Adding unique constraint on 'TestStatus', fields ['name']
        db.create_unique(u'ava_core_teststatus', ['name'])

        # Adding unique constraint on 'SystemConfig', fields ['name']
        db.create_unique(u'ava_core_systemconfig', ['name'])

        # Adding unique constraint on 'Role', fields ['name']
        db.create_unique(u'ava_core_role', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Role', fields ['name']
        db.delete_unique(u'ava_core_role', ['name'])

        # Removing unique constraint on 'SystemConfig', fields ['name']
        db.delete_unique(u'ava_core_systemconfig', ['name'])

        # Removing unique constraint on 'TestStatus', fields ['name']
        db.delete_unique(u'ava_core_teststatus', ['name'])

        # Removing unique constraint on 'UserStatus', fields ['name']
        db.delete_unique(u'ava_core_userstatus', ['name'])

        # Removing unique constraint on 'Module', fields ['name']
        db.delete_unique(u'ava_core_module', ['name'])

        # Removing unique constraint on 'UserPreference', fields ['name']
        db.delete_unique(u'ava_core_userpreference', ['name'])

        # Removing unique constraint on 'GeneralStatus', fields ['name']
        db.delete_unique(u'ava_core_generalstatus', ['name'])

        # Removing unique constraint on 'Mode', fields ['name']
        db.delete_unique(u'ava_core_mode', ['name'])

        # Removing unique constraint on 'Group', fields ['name']
        db.delete_unique(u'ava_core_group', ['name'])


    models = {
        u'ava_core.generalstatus': {
            'Meta': {'object_name': 'GeneralStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.mode': {
            'Meta': {'object_name': 'Mode'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.module': {
            'Meta': {'object_name': 'Module'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enabled': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.role': {
            'Meta': {'object_name': 'Role'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.teststatus': {
            'Meta': {'object_name': 'TestStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core.user': {
            'Meta': {'object_name': 'User'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core.Role']", 'symmetrical': 'False'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'userstatus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core.UserStatus']"})
        },
        u'ava_core.userpreference': {
            'Meta': {'object_name': 'UserPreference'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.userstatus': {
            'Meta': {'object_name': 'UserStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['ava_core']