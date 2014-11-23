from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.ava_core_org.models import Organisation, OrganisationUnit
from apps.ava_core_org.forms import OrganisationForm, OrganisationUnitForm
from django.contrib.auth.models import User
from apps.ava_core_org.forms import  *


class OrganisationIndexView(generic.ListView):
    template_name = 'org/index.html'
    context_object_name = 'org_list'

    def get_queryset(self):
        """Return the last five created org."""
        self.request.session['organisation']=None 
        return Organisation.objects.filter(user=self.request.user,project=self.request.session['project'])

class OrganisationDetailView(generic.DetailView):
    model = Organisation
    context_object_name = 'organisation'
    template_name = 'org/view.html'

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetailView, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        id_count=0
        organisation = get_object_or_404(Organisation, pk=pk)
        people = Person.objects.filter(organisation=organisation)
        for p in people:
            fish = p.identifier_set.all().count()
            id_count = id_count + fish

        context['org_identifier_count'] = id_count

        return context

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            organisation = get_object_or_404(Organisation, pk=pk)
            request.session['organisation']=organisation.id
        return super(OrganisationDetailView,self).get(self, request, *args, **kwargs)

class OrganisationDeleteView(DeleteView):
    model = Organisation
    template_name = 'confirm_delete.html'
    success_url = '/org/'


class OrganisationCreateView(CreateView):
    model = Organisation
    form_class = OrganisationForm
    template_name = 'org/organisation.html'
    success_url = '/org/'

    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        if (form.is_valid()):
                return self.form_valid(form)
        else:
            print form.errors
            return self.form_invalid(form)

    def form_valid(self, form):
        project_id = self.request.session['project']
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.project = project
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else: 
            # TO Do
            return HttpResponseRedirect(self.get_success_url()) 

    def form_invalid(self,form):
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(OrganisationCreateView, self).get_context_data(**kwargs)
        context['form'] = OrganisationForm
        return context

class OrganisationUpdateView(UpdateView):
    model = Organisation
    template_name = 'item.html'
    success_url = '/'
    form_class = OrganisationForm
    page_title = 'Update organisation'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(OrganisationUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

class OrganisationUnitUpdateView(CreateView):
    model=OrganisationUnit    
    template_name = 'org/organisationunit.html'
    form_class = OrganisationUnitForm

    def get_context_data(self, **kwargs):
        context = super(OrganisationUnitUpdateView, self).get_context_data(**kwargs)
        context['form'] = OrganisationUnitForm()
        pk = self.request.session['organisation']
        context['unit_list'] = OrganisationUnit.objects.filter(organisation__id=pk)
        return context

    def get_queryset(self):
        pk = self.request.session['organisation']
        return OrganisationUnit.objects.filter(organisation__id=pk)

    def form_valid(self, form):
        self.object = form.save()
        pk = self.object.organisation.id
        success_url = '/org//chart/'
        return HttpResponseRedirect(success_url)

