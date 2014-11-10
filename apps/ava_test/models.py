from django.db import models
from django.contrib.auth.models import User
from apps.ava_core.models import TimeStampedModel,ReferenceModel
from apps.ava_core_org.models import Organisation

class Test(TimeStampedModel):
    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)
    testtype = models.ForeignKey('TestType', null=False)
    timingtype = models.ForeignKey('TimingType', null=False)
    org = models.ForeignKey('ava_core_org.Organisation', null=False)

    def __unicode__(self):
        return self.name or u''


class TestType (ReferenceModel):
    url= models.TextField(max_length="50", null=False)

class TimingType (ReferenceModel):
    pass




