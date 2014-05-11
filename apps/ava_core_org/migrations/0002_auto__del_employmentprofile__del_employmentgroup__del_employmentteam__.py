# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EmploymentProfile'
        db.delete_table(u'ava_core_org_employmentprofile')

        # Deleting model 'EmploymentGroup'
        db.delete_table(u'ava_core_org_employmentgroup')

        # Deleting model 'EmploymentTeam'
        db.delete_table(u'ava_core_org_employmentteam')

        # Adding model 'Employee'
        db.create_table(u'ava_core_org_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Department'], null=True)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['Employee'])

        # Adding M2M table for field team on 'Employee'
        m2m_table_name = db.shorten_name(u'ava_core_org_employee_team')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'ava_core_org.employee'], null=False)),
            ('team', models.ForeignKey(orm[u'ava_core_org.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employee_id', 'team_id'])

        # Adding M2M table for field group on 'Employee'
        m2m_table_name = db.shorten_name(u'ava_core_org_employee_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'ava_core_org.employee'], null=False)),
            ('group', models.ForeignKey(orm[u'ava_core_org.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employee_id', 'group_id'])


    def backwards(self, orm):
        # Adding model 'EmploymentProfile'
        db.create_table(u'ava_core_org_employmentprofile', (
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Office'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Department'], null=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Organisation'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentProfile'])

        # Adding model 'EmploymentGroup'
        db.create_table(u'ava_core_org_employmentgroup', (
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Group'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentGroup'])

        # Adding model 'EmploymentTeam'
        db.create_table(u'ava_core_org_employmentteam', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_org.Team'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ava_core_org', ['EmploymentTeam'])

        # Deleting model 'Employee'
        db.delete_table(u'ava_core_org_employee')

        # Removing M2M table for field team on 'Employee'
        db.delete_table(db.shorten_name(u'ava_core_org_employee_team'))

        # Removing M2M table for field group on 'Employee'
        db.delete_table(db.shorten_name(u'ava_core_org_employee_group'))


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
        u'ava_core_org.employee': {
            'Meta': {'object_name': 'Employee'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Department']", 'null': 'True'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core_org.Group']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Office']", 'null': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_org.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ava_core_org.Team']", 'null': 'True', 'symmetrical': 'False'})
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