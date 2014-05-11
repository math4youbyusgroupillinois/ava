# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ActiveDirectoryPerson', fields ['objectGUID', 'objectSid']
        db.delete_unique(u'module_activedirectory_activedirectoryperson', ['objectGUID', 'objectSid'])

        # Deleting model 'ActiveDirectoryPerson'
        db.delete_table(u'module_activedirectory_activedirectoryperson')

        # Removing M2M table for field group on 'ActiveDirectoryPerson'
        db.delete_table(db.shorten_name(u'module_activedirectory_activedirectoryperson_group'))

        # Adding model 'ActiveDirectoryUser'
        db.create_table(u'module_activedirectory_activedirectoryuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
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
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('queryParameters', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['module_activedirectory.QueryParameters'])),
        ))
        db.send_create_signal(u'module_activedirectory', ['ActiveDirectoryUser'])

        # Adding M2M table for field group on 'ActiveDirectoryUser'
        m2m_table_name = db.shorten_name(u'module_activedirectory_activedirectoryuser_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activedirectoryuser', models.ForeignKey(orm[u'module_activedirectory.activedirectoryuser'], null=False)),
            ('activedirectorygroup', models.ForeignKey(orm[u'module_activedirectory.activedirectorygroup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activedirectoryuser_id', 'activedirectorygroup_id'])

        # Adding unique constraint on 'ActiveDirectoryUser', fields ['objectGUID', 'objectSid']
        db.create_unique(u'module_activedirectory_activedirectoryuser', ['objectGUID', 'objectSid'])

        # Adding field 'ActiveDirectoryGroup.user'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'ActiveDirectoryGroup.queryParameters'
        db.add_column(u'module_activedirectory_activedirectorygroup', 'queryParameters',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['module_activedirectory.QueryParameters']),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'ActiveDirectoryUser', fields ['objectGUID', 'objectSid']
        db.delete_unique(u'module_activedirectory_activedirectoryuser', ['objectGUID', 'objectSid'])

        # Adding model 'ActiveDirectoryPerson'
        db.create_table(u'module_activedirectory_activedirectoryperson', (
            ('primaryGroupID', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('isCriticalSystemObject', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('logonCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('cn', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('adminCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lastLogonTimestamp', self.gf('django.db.models.fields.CharField')(max_length=300)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sAMAccountName', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('sAMAccountType', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('logonHours', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('objectSid', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('whenCreated', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('uSNCreated', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('accountExpire', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('badPasswordTime', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('dn', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pwdLastSet', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('objectGUID', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('whenChanged', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('badPwdCount', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('displayName', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('userAccountControl', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lastLogon', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('uSNChanged', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lastLogoff', self.gf('django.db.models.fields.CharField')(max_length=300)),
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

        # Adding unique constraint on 'ActiveDirectoryPerson', fields ['objectGUID', 'objectSid']
        db.create_unique(u'module_activedirectory_activedirectoryperson', ['objectGUID', 'objectSid'])

        # Deleting model 'ActiveDirectoryUser'
        db.delete_table(u'module_activedirectory_activedirectoryuser')

        # Removing M2M table for field group on 'ActiveDirectoryUser'
        db.delete_table(db.shorten_name(u'module_activedirectory_activedirectoryuser_group'))

        # Deleting field 'ActiveDirectoryGroup.user'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'user_id')

        # Deleting field 'ActiveDirectoryGroup.queryParameters'
        db.delete_column(u'module_activedirectory_activedirectorygroup', 'queryParameters_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'module_activedirectory.activedirectorygroup': {
            'Meta': {'object_name': 'ActiveDirectoryGroup'},
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distinguishedName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objectCategory': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'queryParameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['module_activedirectory.QueryParameters']"}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'module_activedirectory.activedirectoryuser': {
            'Meta': {'unique_together': "(('objectGUID', 'objectSid'),)", 'object_name': 'ActiveDirectoryUser'},
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
            'queryParameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['module_activedirectory.QueryParameters']"}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sAMAccountType': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userAccountControl': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'module_activedirectory.queryparameters': {
            'Meta': {'unique_together': "(('user', 'server', 'user_dn'),)", 'object_name': 'QueryParameters'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dump_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_pw': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['module_activedirectory']