# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'OrganisationSize', fields ['name']
        db.create_unique(u'ava_core_org_organisationsize', ['name'])

        # Adding unique constraint on 'OrganisationGroupType', fields ['name']
        db.create_unique(u'ava_core_org_organisationgrouptype', ['name'])

        # Adding unique constraint on 'OrganisationUnitType', fields ['name']
        db.create_unique(u'ava_core_org_organisationunittype', ['name'])

        # Adding unique constraint on 'Industry', fields ['name']
        db.create_unique(u'ava_core_org_industry', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Industry', fields ['name']
        db.delete_unique(u'ava_core_org_industry', ['name'])

        # Removing unique constraint on 'OrganisationUnitType', fields ['name']
        db.delete_unique(u'ava_core_org_organisationunittype', ['name'])

        # Removing unique constraint on 'OrganisationGroupType', fields ['name']
        db.delete_unique(u'ava_core_org_organisationgrouptype', ['name'])

        # Removing unique constraint on 'OrganisationSize', fields ['name']
        db.delete_unique(u'ava_core_org_organisationsize', ['name'])


    models = {
        u'ava_core_org.address': {
            'Meta': {'object_name': 'Address'},
            'buildingname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'buildingnumber': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'floor': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'poboxnumber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'streetnumber': ('django.db.models.fields.IntegerField', [], {}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ava_core_org.country': {
            'Meta': {'object_name': 'Country'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ava_core_org.dialingcode': {
            'Meta': {'object_name': 'DialingCode'},
            'areacode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intcode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
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
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Address']"}),
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
        u'ava_core_org.telephone': {
            'Meta': {'object_name': 'Telephone'},
            'countrycode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.DialingCode']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True', 'blank': 'True'})
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