from django.db import models
from django.core.validators import validate_email,validate_slug,validate_ipv46_address
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

from ava_core.models import TimeStampedModel
from ava_core_project.models import Project

# CORE TABLES: TARGETS


class Person(TimeStampedModel):
    firstname = models.CharField(max_length=75,validators=[validate_slug])
    surname = models.CharField(max_length=75,validators=[validate_slug])
    user = models.ForeignKey(User)
    project = models.ForeignKey('ava_core_project.Project')

    def __unicode__(self):
        return self.firstname+" "+self.surname or u''
    
    class Meta:
        verbose_name = ('person')
        verbose_name_plural = ('people')

class Identifier(TimeStampedModel):

    EMAIL = 'EMAIL'
    SKYPE = 'SKYPE'
    IP = 'IPADD'
    UNAME = 'UNAME'

    IDENTIFIER_TYPE_CHOICES = (
        (EMAIL,  'Email Address'),
        (SKYPE,  'Skype ID'),
        (IP,  'IP Address'),
        (UNAME, 'Username'),
    )

    identifier = models.CharField(max_length=100)
    identifiertype = models.CharField(max_length=5,
                            choices=IDENTIFIER_TYPE_CHOICES, default=EMAIL,
                                verbose_name='Identifier Type')
    person = models.ForeignKey('Person', null=False)

    class Meta:
        unique_together = ("identifier", "identifiertype","person")


    def __unicode_(self):
        return self.identifier or u''

    def clean(self):
        if self.identifiertype == 'EMAIL':
            try:
                validate_email(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as EMAIL but does not contain a valid email address')
        
        if self.identifiertype == 'IPADD':
            try:
                validate_ipv46_address(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as IP ADDRESS but does not contain a valid ip4/ip6 address')
        
        if self.identifiertype == 'UNAME' or self.identifiertype =='SKYPE':
            try:
                validate_slug(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as USERNAME/SKYPE but does not contain a username or skype identifier')
        

class ExtendedProfile(TimeStampedModel):
    dob = models.DateField()
    person = models.OneToOneField('Person', null=False)
    title = models.CharField(max_length = 255)
    notes = models.TextField()

