from django.db import models

from apps.ava_core.models import TimeStampedModel

class Identity(TimeStampedModel):
    comment = models.TextField(null=True)
    name = models.CharField(null=True,max_length=50)
    
    def __unicode__(self):
        return self.id or u''
    
    class Meta:
        verbose_name = ('identity')
        verbose_name_plural = ('identities')

