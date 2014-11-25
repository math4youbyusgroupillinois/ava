from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from apps.ava_test_email.models import EmailTest, EmailTestTarget
from apps.ava_test_email.forms import  EmailTestForm, EmailTargetForm
from apps.ava_core_people.models import Person, Identifier



class EmailTestIndexView(generic.ListView):
    template_name = 'email/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test']=None
        return EmailTest.objects.filter(user=self.request.user)

class EmailTestDetailView(generic.DetailView):
    model = EmailTest
    context_object_name = 'test'
    template_name = 'email/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(EmailTest, pk=pk)
            request.session['test']=test.id
        return super(EmailTestDetailView,self).get(self, request, *args, **kwargs)

class EmailTestDeleteView(DeleteView):
    model = EmailTest
    template_name = 'confirm_delete.html'
    success_url = '/test/email/'

class EmailTestCreateView(CreateView):
    model = EmailTest
    template_name = 'email/list_modal.html'
    success_url = '/test/email/'
    form_class = EmailTestForm
    page_title = 'Add a new email test'
    button_value = 'Add email test'
    item_type = 'email test'

    def get_context_data(self, **kwargs):
        context = super(EmailTestCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['form_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.add_targets()
        return HttpResponseRedirect(self.get_success_url())

    def add_targets(self):
        test = self.object
        organisation = test.org
        people = organisation.person_set.all()
        for p in people:
            ids = p.identifier_set.all()
            for i in ids:
                if i.identifiertype == Identifier.EMAIL:
                    obj, created = EmailTestTarget.objects.get_or_create(target=i,emailtest=test)
                    test = EmailTestTarget
        return "OK"

    #i#def generate_token(self):


class EmailTestUpdateView(UpdateView):
    model = EmailTest
    template_name = 'item.html'
    success_url = '/test/email/'
    form_class = EmailTestForm
    page_title = 'Update email test details'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(EmailTestUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context


