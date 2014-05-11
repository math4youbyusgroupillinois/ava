from django.db import models
from ava_core.models import TimeStampedModel, ReferenceModel, ConfigurationModel
from django.contrib.auth.models import User

class Project(TimeStampedModel):
    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)

    def __unicode__(self):
        return self.name or u''
    
#class ProjectRole(ReferenceModel):
#    pass

class ProjectTeamMembers(TimeStampedModel):
    project=model.ForeignKey('Project')
    user=model.ForeignKey(User)

    def __unicode__(self):
        return self.user or u''
    
