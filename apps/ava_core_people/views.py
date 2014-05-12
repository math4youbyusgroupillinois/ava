from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from apps.ava_core_people.models import Person, Identifier
from apps.ava_core_project.models import Project
from apps.ava_core_people.forms import IdentifierFormSet, PersonForm


class PersonIndexView(generic.ListView):
    template_name = 'people/index.html'
    context_object_name = 'people_list'

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)


class PersonDetailView(generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/view.html'


class IdentifierUpdateView(UpdateView):
        model = Identifier
        fields = ['identifier', 'identifiertype']
        template_name = 'people/identifier_update_form.html'
        success_url = '/people/'


class IdentifierDeleteView(DeleteView):
        model = Identifier
        template_name = 'people/identifier_confirm_delete.html'
        success_url = '/people/'


class PersonDeleteView(DeleteView):
        model = Person
        template_name = 'people/person_confirm_delete.html'
        success_url = '/people/'


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'people/person.html'
    form_class = PersonForm
    success_url = '/people/'
    page_title = 'update'
    button_value = 'Update Person'

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        person_pk = self.kwargs.get('pk')
        if person_pk:
            instance = get_object_or_404(Person, pk=person_pk)
            if self.request.POST:
                context['identifier_form'] = IdentifierFormSet(
                        self.request.POST, instance=instance)
                context['form'] = PersonForm(self.request.POST,
                        instance=instance)
            else:
                context['form'] = PersonForm(instance=instance)
                context['identifier_form'] = IdentifierFormSet(instance=instance)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['identifier_form']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form,
                    identifier_form=formset, page_title=self.page_title,
                                  button_value=self.button_value))


class PersonCreateView(CreateView):
    template_name = 'people/person.html'
    model = Person
    form_class = PersonForm
    success_url = '/people/'
    page_title = 'new'
    button_value = 'Add Person'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        identifier_form = IdentifierFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                identifier_form=identifier_form,
                page_title=self.page_title, button_value=self.button_value))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        person = form.save(commit=False)
        identifier_form = IdentifierFormSet(self.request.POST, instance=person)
        if (form.is_valid() and identifier_form.is_valid()):
            return self.form_valid(form, identifier_form)
        else:
            return self.form_invalid(form, identifier_form)

    def form_valid(self, form, identifier_form):
        project_id = self.request.session['project']
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.project = project
            self.object.save()
            identifier_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            # TO DO
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, identifier_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                identifier_form=identifier_form,
                page_title=self.page_title, button_value=self.button_value))
