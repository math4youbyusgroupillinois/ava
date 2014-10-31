from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from apps.ava_core_project.models import Project
from apps.ava_core_project.forms import  ProjectForm

class DashboardView(generic.ListView):
    template_name = 'project/home.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['project']=None 
        return Project.objects.filter(user=self.request.user)


class ProjectIndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['project']=None 
        return Project.objects.filter(user=self.request.user)

class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            project = get_object_or_404(Project, pk=pk)
            request.session['project']=project.id
        return super(ProjectDetailView,self).get(self, request, *args, **kwargs)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'confirm_delete.html'
    success_url = '/project/'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/list_modal.html'
    success_url = '/project/'
    form_class = ProjectForm
    page_title = 'Add a new project'
    button_value = 'Add project'
    item_type = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['form_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'item.html'
    success_url = '/project/'
    form_class = ProjectForm
    page_title = 'Update project details'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context
