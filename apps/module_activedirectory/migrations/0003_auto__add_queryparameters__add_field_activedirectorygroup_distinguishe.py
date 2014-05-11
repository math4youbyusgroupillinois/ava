# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QueryParameters'
        db.create_table(u'module_activedirectory_queryparameters', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user_dn', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_pw', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dump_dn', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'module_activedirectory', ['QueryParameters'])

        # Adding field 'ActiveDirectoryGroup.distinguishedName'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'distinguishedName',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=300),
                      keep_default=False)

        # Adding field 'ActiveDirectoryGroup.name'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'name',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'ActiveDirectoryGroup.objectCategory'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'objectCategory',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=30),
                      keep_default=False)

        # Adding field 'ActiveDirectoryGroup.sAMAccountName'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'sAMAccountName',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'QueryParameters'
        db.delete_table(u'module_activedirectory_queryparameters')

        # Deleting field 'ActiveDirectoryGroup.distinguishedName'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'distinguishedName')

        # Deleting field 'ActiveDirectoryGroup.name'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'name')

        # Deleting field 'ActiveDirectoryGroup.objectCategory'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'objectCategory')

        # Deleting field 'ActiveDirectoryGroup.sAMAccountName'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'sAMAccountName')


    models = {
        u'module_activedirectory.activedirectorygroup': {
            'Meta': {'object_name': 'ActiveDirectoryGroup'},
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distinguishedName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objectCategory': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
        },
        u'module_activedirectory.queryparameters': {
            'Meta': {'object_name': 'QueryParameters'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dump_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_pw': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['module_activedirectory']