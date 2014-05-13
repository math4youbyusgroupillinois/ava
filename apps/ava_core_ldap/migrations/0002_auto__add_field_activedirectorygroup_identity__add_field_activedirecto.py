# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ActiveDirectoryGroup.identity'
        db.add_column(u'ava_core_ldap_activedirectorygroup', 'identity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_identity.Identity'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActiveDirectoryUser.identity'
        db.add_column(u'ava_core_ldap_activedirectoryuser', 'identity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_identity.Identity'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ActiveDirectoryGroup.identity'
        db.delete_column(u'ava_core_ldap_activedirectorygroup', 'identity_id')

        # Deleting field 'ActiveDirectoryUser.identity'
        db.delete_column(u'ava_core_ldap_activedirectoryuser', 'identity_id')


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
        u'ava_core_identity.identity': {
            'Meta': {'object_name': 'Identity'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'ava_core_ldap.activedirectorygroup': {
            'Meta': {'unique_together': "(('objectGUID', 'objectSid'),)", 'object_name': 'ActiveDirectoryGroup'},
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'distinguishedName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_identity.Identity']", 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core_ldap.ActiveDirectoryUser']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objectCategory': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectGUID': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectSid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'queryParameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_ldap.QueryParameters']"}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ava_core_ldap.activedirectoryuser': {
            'Meta': {'unique_together': "(('objectGUID', 'objectSid'),)", 'object_name': 'ActiveDirectoryUser'},
            'accountExpire': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'adminCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'badPasswordTime': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'badPwdCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'cn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'distinguishedName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dn': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_identity.Identity']", 'null': 'True', 'blank': 'True'}),
            'isCriticalSystemObject': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogoff': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogon': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'lastLogonTimestamp': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'logonCount': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'logonHours': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'memberOf': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core_ldap.ActiveDirectoryGroup']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectGUID': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'objectSid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'primaryGroupID': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pwdLastSet': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'queryParameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_ldap.QueryParameters']"}),
            'sAMAccountName': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sAMAccountType': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uSNCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userAccountControl': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenChanged': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whenCreated': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'ava_core_ldap.queryparameters': {
            'Meta': {'unique_together': "(('user', 'server', 'user_dn'),)", 'object_name': 'QueryParameters'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dump_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_dn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_pw': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ava_core_org.industry': {
            'Meta': {'object_name': 'Industry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core_org.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Industry']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_project.Project']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationSize']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ava_core_org.organisationsize': {
            'Meta': {'object_name': 'OrganisationSize'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core_project.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ava_core_ldap']