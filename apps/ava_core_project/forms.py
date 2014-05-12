from django.forms import ModelForm, Form
from apps.ava_core_project.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name',  'description')

