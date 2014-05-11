# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserStatus'
        db.create_table(u'ava_core_userstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['UserStatus'])

        # Adding model 'Role'
        db.create_table(u'ava_core_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['Role'])

        # Adding model 'Mode'
        db.create_table(u'ava_core_mode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['Mode'])

        # Adding model 'TestStatus'
        db.create_table(u'ava_core_teststatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['TestStatus'])

        # Adding model 'Group'
        db.create_table(u'ava_core_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['Group'])

        # Adding model 'GeneralStatus'
        db.create_table(u'ava_core_generalstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['GeneralStatus'])

        # Adding model 'Module'
        db.create_table(u'ava_core_module', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('enabled', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
        ))
        db.send_create_signal(u'ava_core', ['Module'])

        # Adding model 'SystemConfig'
        db.create_table(u'ava_core_systemconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['SystemConfig'])

        # Adding model 'UserPreference'
        db.create_table(u'ava_core_userpreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core', ['UserPreference'])

        # Adding model 'User'
        db.create_table(u'ava_core_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('userstatus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core.UserStatus'])),
        ))
        db.send_create_signal(u'ava_core', ['User'])

        # Adding M2M table for field roles on 'User'
        m2m_table_name = db.shorten_name(u'ava_core_user_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'ava_core.user'], null=False)),
            ('role', models.ForeignKey(orm[u'ava_core.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'role_id'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'ava_core_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'ava_core.user'], null=False)),
            ('group', models.ForeignKey(orm[u'ava_core.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])


    def backwards(self, orm):
        # Deleting model 'UserStatus'
        db.delete_table(u'ava_core_userstatus')

        # Deleting model 'Role'
        db.delete_table(u'ava_core_role')

        # Deleting model 'Mode'
        db.delete_table(u'ava_core_mode')

        # Deleting model 'TestStatus'
        db.delete_table(u'ava_core_teststatus')

        # Deleting model 'Group'
        db.delete_table(u'ava_core_group')

        # Deleting model 'GeneralStatus'
        db.delete_table(u'ava_core_generalstatus')

        # Deleting model 'Module'
        db.delete_table(u'ava_core_module')

        # Deleting model 'SystemConfig'
        db.delete_table(u'ava_core_systemconfig')

        # Deleting model 'UserPreference'
        db.delete_table(u'ava_core_userpreference')

        # Deleting model 'User'
        db.delete_table(u'ava_core_user')

        # Removing M2M table for field roles on 'User'
        db.delete_table(db.shorten_name(u'ava_core_user_roles'))

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'ava_core_user_groups'))


    models = {
        u'ava_core.generalstatus': {
            'Meta': {'object_name': 'GeneralStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core.mode': {
            'Meta': {'object_name': 'Mode'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core.module': {
            'Meta': {'object_name': 'Module'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enabled': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core.role': {
            'Meta': {'object_name': 'Role'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core.systemconfig': {
            'Meta': {'object_name': 'SystemConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.teststatus': {
            'Meta': {'object_name': 'TestStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
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
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ava_core.userstatus': {
            'Meta': {'object_name': 'UserStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        }
    }

    complete_apps = ['ava_core']