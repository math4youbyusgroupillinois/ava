# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TwitterMessageType'
        db.delete_table(u'ava_test_twitter_twittermessagetype')

        # Deleting field 'TwitterTest.token'
        db.delete_column(u'ava_test_twitter_twittertest', 'token')

        # Deleting field 'TwitterTest.user'
        db.delete_column(u'ava_test_twitter_twittertest', 'user_id')

        # Deleting field 'TwitterTest.created'
        db.delete_column(u'ava_test_twitter_twittertest', 'created')

        # Deleting field 'TwitterTest.test'
        db.delete_column(u'ava_test_twitter_twittertest', 'test_id')

        # Deleting field 'TwitterTest.testtype'
        db.delete_column(u'ava_test_twitter_twittertest', 'testtype_id')

        # Deleting field 'TwitterTest.id'
        db.delete_column(u'ava_test_twitter_twittertest', u'id')

        # Deleting field 'TwitterTest.modified'
        db.delete_column(u'ava_test_twitter_twittertest', 'modified')

        # Adding field 'TwitterTest.test_ptr'
        db.add_column(u'ava_test_twitter_twittertest', u'test_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['ava_test.Test'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'TwitterTest.twittertesttype'
        db.add_column(u'ava_test_twitter_twittertest', 'twittertesttype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ava_test_twitter.TwitterTestType']),
                      keep_default=False)

        # Adding field 'TwitterTest.twitteraccount'
        db.add_column(u'ava_test_twitter_twittertest', 'twitteraccount',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ava_test_twitter.TwitterAccount']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'TwitterMessageType'
        db.create_table(u'ava_test_twitter_twittermessagetype', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
        ))
        db.send_create_signal(u'ava_test_twitter', ['TwitterMessageType'])

        # Adding field 'TwitterTest.token'
        db.add_column(u'ava_test_twitter_twittertest', 'token',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'TwitterTest.user'
        db.add_column(u'ava_test_twitter_twittertest', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'TwitterTest.created'
        db.add_column(u'ava_test_twitter_twittertest', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=2, blank=True),
                      keep_default=False)

        # Adding field 'TwitterTest.test'
        db.add_column(u'ava_test_twitter_twittertest', 'test',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ava_test.Test']),
                      keep_default=False)

        # Adding field 'TwitterTest.testtype'
        db.add_column(u'ava_test_twitter_twittertest', 'testtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ava_test_twitter.TwitterTestType']),
                      keep_default=False)

        # Adding field 'TwitterTest.id'
        db.add_column(u'ava_test_twitter_twittertest', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=2, primary_key=True),
                      keep_default=False)

        # Adding field 'TwitterTest.modified'
        db.add_column(u'ava_test_twitter_twittertest', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=2, blank=True),
                      keep_default=False)

        # Deleting field 'TwitterTest.test_ptr'
        db.delete_column(u'ava_test_twitter_twittertest', u'test_ptr_id')

        # Deleting field 'TwitterTest.twittertesttype'
        db.delete_column(u'ava_test_twitter_twittertest', 'twittertesttype_id')

        # Deleting field 'TwitterTest.twitteraccount'
        db.delete_column(u'ava_test_twitter_twittertest', 'twitteraccount_id')


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
        u'ava_test.test': {
            'Meta': {'object_name': 'Test'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'testtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test.TestType']"}),
            'timingtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test.TimingType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ava_test.testtype': {
            'Meta': {'object_name': 'TestType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_test.timingtype': {
            'Meta': {'object_name': 'TimingType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_test_twitter.tweetlink': {
            'Meta': {'object_name': 'TweetLink'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_test_twitter.tweettemplate': {
            'Meta': {'object_name': 'TweetTemplate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'tweet': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        },
        u'ava_test_twitter.twitteraccount': {
            'Meta': {'object_name': 'TwitterAccount'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'password_enc': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ava_test_twitter.twittertest': {
            'Meta': {'object_name': 'TwitterTest', '_ormbases': [u'ava_test.Test']},
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test_twitter.TweetLink']"}),
            u'test_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ava_test.Test']", 'unique': 'True', 'primary_key': 'True'}),
            'tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test_twitter.TweetTemplate']"}),
            'twitteraccount': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test_twitter.TwitterAccount']"}),
            'twittertesttype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_test_twitter.TwitterTestType']"})
        },
        u'ava_test_twitter.twittertesttype': {
            'Meta': {'object_name': 'TwitterTestType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ava_test_twitter']