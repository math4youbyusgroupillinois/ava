from django.db import models
from django.core.validators import validate_slug,validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from apps.ava_core.models import TimeStampedModel,ReferenceModel
from apps.ava_core_people.models import Person
from apps.ava_core_project.models import Project

# CORE TABLES: TARGETS

class OrganisationGroupType (ReferenceModel):
    pass

class Industry (ReferenceModel):
    pass

class OrganisationUnitType (ReferenceModel):
    pass

class OrganisationSize (ReferenceModel):
    pass

class Organisation (TimeStampedModel):
    name = models.CharField(max_length=100)
    industry = models.ForeignKey('Industry', null=False)
    size= models.ForeignKey('OrganisationSize', null=False)
    user = models.ForeignKey(User)
    project = models.ForeignKey('ava_core_project.Project')

    def __unicode__(self):
        return self.name or u''

class OrganisationUnit (TimeStampedModel):
    name = models.CharField(max_length=100)
    unittype = models.ForeignKey('OrganisationUnitType', null=False)
    office=models.ForeignKey('Office', null=True, blank=True)
    organisation = models.ForeignKey('Organisation', null=False)
    parent=models.ForeignKey('OrganisationUnit', null=True, blank=True);

    def __unicode__(self):
        return self.name or u''

class OrganisationGroup (TimeStampedModel):
    name = models.CharField(max_length=100)
    grouptype = models.ForeignKey('OrganisationGroupType', null=False)
    organisation = models.ForeignKey('Organisation', null=False)

    def __unicode__(self):
        return self.name or u''


class Office (TimeStampedModel):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    #address= models.ForeignKey('ava_ref_location.Address', null=False)
    organisation= models.ForeignKey('Organisation', null=False)
    headoffice = models.BooleanField()

    def __unicode__(self):
        return self.name or u''

class Website (TimeStampedModel):
    url=models.URLField()
    port=models.PositiveIntegerField()
    https=models.BooleanField()
    organisation = models.ForeignKey('Organisation', null=False)

    def __unicode__(self):
        return self.url or u''

class OrganisationIdentifier(TimeStampedModel):
    
    IDENTIFIER_TYPE_CHOICES = (
        ('EMAIL',  'Email Address'),
        ('SKYPE',  'Skype ID'),
        ('IP',  'IP Address'),
    )
    
    organisation = models.ForeignKey('Organisation', null=False) 
    organisationunit = models.ForeignKey('OrganisationUnit', null=True, blank=True)
    identifier = models.CharField(max_length=100)
    identifiertype = models.CharField(max_length=5,
                            choices=IDENTIFIER_TYPE_CHOICES, default='EMAIL',
                                verbose_name='Identifier Type')

    def __unicode__(self):
        return self.identifier or u''

class Employee(TimeStampedModel):
    person = models.ForeignKey('ava_core_people.Person', null=False)
    organisationunit = models.ForeignKey('OrganisationUnit', null=True, blank=True)
    organisation = models.ForeignKey('Organisation', null=False) 
    office = models.ForeignKey('Office', null=True, blank=True)
    group = models.ManyToManyField('OrganisationGroup',null=True, blank=True)

    def __unicode__(self):
        return self.person.firstname+' '+ self.person.surname or u''

