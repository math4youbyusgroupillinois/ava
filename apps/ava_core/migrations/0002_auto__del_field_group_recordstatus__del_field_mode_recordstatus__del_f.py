# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Group.recordstatus'
        db.delete_column(u'ava_core_group', 'recordstatus')

        # Deleting field 'Mode.recordstatus'
        db.delete_column(u'ava_core_mode', 'recordstatus')

        # Deleting field 'GeneralStatus.recordstatus'
        db.delete_column(u'ava_core_generalstatus', 'recordstatus')

        # Deleting field 'UserPreference.recordstatus'
        db.delete_column(u'ava_core_userpreference', 'recordstatus')

        # Deleting field 'Module.recordstatus'
        db.delete_column(u'ava_core_module', 'recordstatus')

        # Deleting field 'UserStatus.recordstatus'
        db.delete_column(u'ava_core_userstatus', 'recordstatus')

        # Deleting field 'TestStatus.recordstatus'
        db.delete_column(u'ava_core_teststatus', 'recordstatus')

        # Deleting field 'SystemConfig.recordstatus'
        db.delete_column(u'ava_core_systemconfig', 'recordstatus')

        # Deleting field 'Role.recordstatus'
        db.delete_column(u'ava_core_role', 'recordstatus')


    def backwards(self, orm):
        # Adding field 'Group.recordstatus'
        db.add_column(u'ava_core_group', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'Mode.recordstatus'
        db.add_column(u'ava_core_mode', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'GeneralStatus.recordstatus'
        db.add_column(u'ava_core_generalstatus', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'UserPreference.recordstatus'
        db.add_column(u'ava_core_userpreference', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'Module.recordstatus'
        db.add_column(u'ava_core_module', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'UserStatus.recordstatus'
        db.add_column(u'ava_core_userstatus', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'TestStatus.recordstatus'
        db.add_column(u'ava_core_teststatus', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'SystemConfig.recordstatus'
        db.add_column(u'ava_core_systemconfig', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'Role.recordstatus'
        db.add_column(u'ava_core_role', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)


    models = {
        u'ava_core.generalstatus': {
            'Meta': {'object_name': 'GeneralStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core.mode': {
            'Meta': {'object_name': 'Mode'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core.module': {
            'Meta': {'object_name': 'Module'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enabled': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core.role': {
            'Meta': {'object_name': 'Role'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.teststatus': {
            'Meta': {'object_name': 'TestStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.userstatus': {
            'Meta': {'object_name': 'UserStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ava_core']