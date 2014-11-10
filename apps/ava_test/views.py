from django.views import generic

from django.shortcuts import redirect, get_object_or_404
from apps.ava_test.models import Test, TestType
from apps.ava_core_org.models import Organisation



class TestIndexView(generic.ListView):
    template_name = 'test/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test']=None
        return Test.objects.filter(user=self.request.user)

class TestOrgIndexView(generic.ListView):
    template_name = 'test/vieworg.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(TestOrgIndexView, self).get_context_data(**kwargs)
        context['test_modules'] = TestType.objects.all()
        context['organisation_id'] = self.request.session['organisation']
        return context

    def get_queryset(self):
        self.request.session['test']=None
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(Organisation, pk=pk)
            self.request.session['organisation']=pk
        return Test.objects.filter(user=self.request.user,org=test)



