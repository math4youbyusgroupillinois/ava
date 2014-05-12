from django.forms import ModelForm, Form
from apps.module_activedirectory.models import QueryParameters


class QueryParametersForm(ModelForm):
    class Meta:
        model = QueryParameters
        fields = ('user_dn','user_pw','dump_dn','server','organisation')
