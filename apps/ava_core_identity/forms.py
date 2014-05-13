from django.forms import ModelForm, Form
from apps.ava_core_identity.models import Identity


class IdentityForm(ModelForm):
    class Meta:
        model = Identity
        fields = ('name',  'comment')

