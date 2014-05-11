# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DialingCode'
        db.delete_table(u'ava_core_org_dialingcode')

        # Deleting model 'Address'
        db.delete_table(u'ava_core_org_address')

        # Deleting model 'Telephone'
        db.delete_table(u'ava_core_org_telephone')

        # Deleting model 'Country'
        db.delete_table(u'ava_core_org_country')

        # Deleting field 'Office.address'
        db.delete_column(u'ava_core_org_office', 'address_id')


    def backwards(self, orm):
        # Adding model 'DialingCode'
        db.create_table(u'ava_core_org_dialingcode', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('areacode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Country'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('intcode', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'ava_core_org', ['DialingCode'])

        # Adding model 'Address'
        db.create_table(u'ava_core_org_address', (
            ('poboxnumber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('streetnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('postalcode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('buildingnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('buildingname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Country'])),
            ('floor', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Address'])

        # Adding model 'Telephone'
        db.create_table(u'ava_core_org_telephone', (
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True, blank=True)),
            ('countrycode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.DialingCode'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Telephone'])

        # Adding model 'Country'
        db.create_table(u'ava_core_org_country', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tld', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Country'])

        # Adding field 'Office.address'
        db.add_column(u'ava_core_org_office', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['ava_core_org.Address']),
                      keep_default=False)


    models = {
        u'ava_core_org.employee': {
            'Meta': {'object_name': 'Employee'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ava_core_org.OrganisationGroup']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'organisationunit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationUnit']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
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
        u'ava_core_org.office': {
            'Meta': {'object_name': 'Office'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'headoffice': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"})
        },
        u'ava_core_org.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Industry']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationSize']"})
        },
        u'ava_core_org.organisationgroup': {
            'Meta': {'object_name': 'OrganisationGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grouptype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationGroupType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"})
        },
        u'ava_core_org.organisationgrouptype': {
            'Meta': {'object_name': 'OrganisationGroupType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core_org.organisationidentifier': {
            'Meta': {'object_name': 'OrganisationIdentifier'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identifiertype': ('django.db.models.fields.CharField', [], {'default': "'EMAIL'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'organisationunit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationUnit']", 'null': 'True', 'blank': 'True'})
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
        u'ava_core_org.organisationunit': {
            'Meta': {'object_name': 'OrganisationUnit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationUnit']", 'null': 'True', 'blank': 'True'}),
            'unittype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.OrganisationUnitType']"})
        },
        u'ava_core_org.organisationunittype': {
            'Meta': {'object_name': 'OrganisationUnitType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'ava_core_org.website': {
            'Meta': {'object_name': 'Website'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'https': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'port': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'ava_core_people.person': {
            'Meta': {'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['ava_core_org']