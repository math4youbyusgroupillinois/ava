from django.db import models
from django.contrib.auth.models import User
from apps.ava_core.models import TimeStampedModel,ReferenceModel
from apps.ava_test.models import Test

class TwitterTest(Test):
    twittertesttype = models.ForeignKey('TwitterTestType', null=False)
    tweet = models.ForeignKey('TweetTemplate', null=False)
    link = models.ForeignKey('TweetLink', null=False)
    twitteraccount = models.ForeignKey('TwitterAccount', null=False)

    def __unicode__(self):
        return self.name or u''


class TwitterTestType (ReferenceModel):
    pass

class TweetTemplate(ReferenceModel):
    tweet = models.TextField(max_length=140)

class TwitterAccount(ReferenceModel):
    username=models.CharField(max_length=100, null=False)
    password_enc = models.TextField(null=False)

class TweetLink(ReferenceModel):
    link = models.URLField()

