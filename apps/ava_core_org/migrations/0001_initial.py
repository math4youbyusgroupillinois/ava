# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroupType'
        db.create_table(u'ava_core_org_grouptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core_org', ['GroupType'])

        # Adding model 'Industry'
        db.create_table(u'ava_core_org_industry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core_org', ['Industry'])

        # Adding model 'TeamType'
        db.create_table(u'ava_core_org_teamtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core_org', ['TeamType'])

        # Adding model 'OrganisationSize'
        db.create_table(u'ava_core_org_organisationsize', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ava_core_org', ['OrganisationSize'])

        # Adding model 'Organisation'
        db.create_table(u'ava_core_org_organisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Industry'])),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.OrganisationSize'])),
        ))
        db.send_create_signal(u'ava_core_org', ['Organisation'])

        # Adding model 'Department'
        db.create_table(u'ava_core_org_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
        ))
        db.send_create_signal(u'ava_core_org', ['Department'])

        # Adding model 'Team'
        db.create_table(u'ava_core_org_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('teamtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.TeamType'])),
            ('teamleader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'], null=True)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Department'], null=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Team'])

        # Adding model 'Group'
        db.create_table(u'ava_core_org_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grouptype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.GroupType'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
        ))
        db.send_create_signal(u'ava_core_org', ['Group'])

        # Adding model 'Address'
        db.create_table(u'ava_core_org_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('buildingnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('buildingname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('streetnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('poboxnumber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('floor', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postalcode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Country'])),
        ))
        db.send_create_signal(u'ava_core_org', ['Address'])

        # Adding model 'Telephone'
        db.create_table(u'ava_core_org_telephone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('countrycode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.DialingCode'])),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Telephone'])

        # Adding model 'Country'
        db.create_table(u'ava_core_org_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tld', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ava_core_org', ['Country'])

        # Adding model 'DialingCode'
        db.create_table(u'ava_core_org_dialingcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Country'])),
            ('intcode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('areacode', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'ava_core_org', ['DialingCode'])

        # Adding model 'Website'
        db.create_table(u'ava_core_org_website', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('port', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('https', self.gf('django.db.models.fields.BooleanField')()),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
        ))
        db.send_create_signal(u'ava_core_org', ['Website'])

        # Adding model 'Office'
        db.create_table(u'ava_core_org_office', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Address'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('headoffice', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ava_core_org', ['Office'])

        # Adding model 'OrganisationIdentifier'
        db.create_table(u'ava_core_org_organisationidentifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Team'], null=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Group'], null=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Department'], null=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('identifiertype', self.gf('django.db.models.fields.CharField')(default='EMAIL', max_length=5)),
        ))
        db.send_create_signal(u'ava_core_org', ['OrganisationIdentifier'])

        # Adding model 'EmploymentProfile'
        db.create_table(u'ava_core_org_employmentprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Department'], null=True)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentProfile'])

        # Adding model 'EmploymentTeam'
        db.create_table(u'ava_core_org_employmentteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Team'])),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentTeam'])

        # Adding model 'EmploymentGroup'
        db.create_table(u'ava_core_org_employmentgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Group'])),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentGroup'])


    def backwards(self, orm):
        # Deleting model 'GroupType'
        db.delete_table(u'ava_core_org_grouptype')

        # Deleting model 'Industry'
        db.delete_table(u'ava_core_org_industry')

        # Deleting model 'TeamType'
        db.delete_table(u'ava_core_org_teamtype')

        # Deleting model 'OrganisationSize'
        db.delete_table(u'ava_core_org_organisationsize')

        # Deleting model 'Organisation'
        db.delete_table(u'ava_core_org_organisation')

        # Deleting model 'Department'
        db.delete_table(u'ava_core_org_department')

        # Deleting model 'Team'
        db.delete_table(u'ava_core_org_team')

        # Deleting model 'Group'
        db.delete_table(u'ava_core_org_group')

        # Deleting model 'Address'
        db.delete_table(u'ava_core_org_address')

        # Deleting model 'Telephone'
        db.delete_table(u'ava_core_org_telephone')

        # Deleting model 'Country'
        db.delete_table(u'ava_core_org_country')

        # Deleting model 'DialingCode'
        db.delete_table(u'ava_core_org_dialingcode')

        # Deleting model 'Website'
        db.delete_table(u'ava_core_org_website')

        # Deleting model 'Office'
        db.delete_table(u'ava_core_org_office')

        # Deleting model 'OrganisationIdentifier'
        db.delete_table(u'ava_core_org_organisationidentifier')

        # Deleting model 'EmploymentProfile'
        db.delete_table(u'ava_core_org_employmentprofile')

        # Deleting model 'EmploymentTeam'
        db.delete_table(u'ava_core_org_employmentteam')

        # Deleting model 'EmploymentGroup'
        db.delete_table(u'ava_core_org_employmentgroup')


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
        u'ava_core_org.department': {
            'Meta': {'object_name': 'Department'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"})
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
        u'ava_core_org.employmentgroup': {
            'Meta': {'object_name': 'EmploymentGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
        },
        u'ava_core_org.employmentprofile': {
            'Meta': {'object_name': 'EmploymentProfile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Department']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
        },
        u'ava_core_org.employmentteam': {
            'Meta': {'object_name': 'EmploymentTeam'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Team']"})
        },
        u'ava_core_org.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grouptype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.GroupType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"})
        },
        u'ava_core_org.grouptype': {
            'Meta': {'object_name': 'GroupType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core_org.industry': {
            'Meta': {'object_name': 'Industry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'ava_core_org.organisationidentifier': {
            'Meta': {'object_name': 'OrganisationIdentifier'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Department']", 'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Group']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identifiertype': ('django.db.models.fields.CharField', [], {'default': "'EMAIL'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Team']", 'null': 'True'})
        },
        u'ava_core_org.organisationsize': {
            'Meta': {'object_name': 'OrganisationSize'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core_org.team': {
            'Meta': {'object_name': 'Team'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Department']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'teamleader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']", 'null': 'True'}),
            'teamtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.TeamType']"})
        },
        u'ava_core_org.teamtype': {
            'Meta': {'object_name': 'TeamType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ava_core_org.telephone': {
            'Meta': {'object_name': 'Telephone'},
            'countrycode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.DialingCode']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"})
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