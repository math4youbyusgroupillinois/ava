from django.forms import ModelForm, Form
from apps.ava_test.models import *


class TestForm(ModelForm):
    class Meta:
        model = Test
        #fields = ('name',  'description', 'testtype', 'timingtype','targettype')