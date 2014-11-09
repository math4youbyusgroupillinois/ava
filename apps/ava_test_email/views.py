from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from apps.ava_test_email.models import EmailTest
from apps.ava_test_email.forms import  EmailTestForm



class EmailTestIndexView(generic.ListView):
    template_name = 'emailtest/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['emailtest']=None
        return EmailTest.objects.filter(user=self.request.user)

class EmailTestDetailView(generic.DetailView):
    model = EmailTest
    context_object_name = 'emailtest'
    template_name = 'emailtest/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            emailtest = get_object_or_404(EmailTest, pk=pk)
            request.session['emailtest']=emailtest.id
        return super(EmailTestDetailView,self).get(self, request, *args, **kwargs)

class EmailTestDeleteView(DeleteView):
    model = EmailTest
    template_name = 'confirm_delete.html'
    success_url = '/emailtest/'

class EmailTestCreateView(CreateView):
    model = EmailTest
    template_name = 'emailtest/list_modal.html'
    success_url = '/emailtest/'
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
        return HttpResponseRedirect(self.get_success_url())


class EmailTestUpdateView(UpdateView):
    model = EmailTest
    template_name = 'item.html'
    success_url = '/emailtest/'
    form_class = EmailTestForm
    page_title = 'Update email test details'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(EmailTestUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

