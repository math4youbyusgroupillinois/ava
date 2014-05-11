# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActiveDirectoryPerson'
        db.create_table(u'module_activedirectory_activedirectoryperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('dn', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('accountExpire', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('adminCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('badPasswordTime', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('badPwdCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('cn', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('displayName', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('isCriticalSystemObject', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lastLogoff', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lastLogon', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lastLogonTimestamp', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('logonCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('logonHours', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('objectGUID', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('objectSid', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('primaryGroupID', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pwdLastSet', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('sAMAccountName', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('sAMAccountType', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('uSNChanged', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('uSNCreated', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('userAccountControl', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('whenChanged', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('whenCreated', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'module_activedirectory', ['ActiveDirectoryPerson'])

        # Adding M2M table for field group on 'ActiveDirectoryPerson'
        m2m_table_name = db.shorten_name(u'module_activedirectory_activedirectoryperson_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activedirectoryperson', models.ForeignKey(orm[u'module_activedirectory.activedirectoryperson'], null=False)),
            ('activedirectorygroup', models.ForeignKey(orm[u'module_activedirectory.activedirectorygroup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activedirectoryperson_id', 'activedirectorygroup_id'])

        # Adding model 'ActiveDirectoryGroup'
        db.create_table(u'module_activedirectory_activedirectorygroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('cn', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'module_activedirectory', ['ActiveDirectoryGroup'])


    def backwards(self, orm):
        # Deleting model 'ActiveDirectoryPerson'
        db.delete_table(u'module_activedirectory_activedirectoryperson')

        # Removing M2M table for field group on 'ActiveDirectoryPerson'
        db.delete_table(db.shorten_name(u'module_activedirectory_activedirectoryperson_group'))

        # Deleting model 'ActiveDirectoryGroup'
        db.delete_table(u'module_activedirectory_activedirectorygroup')


    models = {
        u'module_activedirectory.activedirectorygroup': {
            'Meta': {'object_name': 'ActiveDirectoryGroup'},
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
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
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'}),
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