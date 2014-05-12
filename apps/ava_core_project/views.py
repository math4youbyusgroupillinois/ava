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
    context_object_name = 'project_list'

    def get_queryset(self):
        self.request.session['project']=None 
        return Project.objects.filter(user=self.request.user)


class ProjectIndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'project_list'

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
    template_name = 'project/project_confirm_delete.html'
    success_url = '/project/'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/project.html'
    success_url = '/project/'
    form_class = ProjectForm
    page_title = 'add'
    button_value = 'add'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        self.request.session['project']=None 
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  page_title=self.page_title,button_value=self.button_value))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates an instance along with
        associated items and then redirects to a
        success page.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  page_title=self.page_title,button_value=self.button_value))

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project.html'
    success_url = '/project/'

