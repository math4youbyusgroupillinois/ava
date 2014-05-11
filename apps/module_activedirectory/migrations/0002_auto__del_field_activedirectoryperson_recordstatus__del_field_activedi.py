# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ActiveDirectoryPerson.recordstatus'
        db.delete_column(u'module_activedirectory_activedirectoryperson', 'recordstatus')

        # Deleting field 'ActiveDirectoryGroup.recordstatus'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'recordstatus')


    def backwards(self, orm):
        # Adding field 'ActiveDirectoryPerson.recordstatus'
        db.add_column(u'module_activedirectory_activedirectoryperson', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'ActiveDirectoryGroup.recordstatus'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)


    models = {
        u'module_activedirectory.activedirectorygroup': {
            'Meta': {'object_name': 'ActiveDirectoryGroup'},
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'module_activedirectory.activedirectoryperson': {
            'Meta': {'object_name': 'ActiveDirectoryPerson'},
            'accountExpire': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'adminCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'badPasswordTime': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'badPwdCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['module_activedirectory.ActiveDirectoryGroup']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCriticalSystemObject': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogoff': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogon': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogonTimestamp': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'logonCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'logonHours': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectGUID': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectSid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'primaryGroupID': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pwdLastSet': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sAMAccountType': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'userAccountControl': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['module_activedirectory']