from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from apps.ava_test_twitter.models import TwitterTest
from apps.ava_test_twitter.forms import  TwitterTestForm
#from twitter import *


class TwitterTestIndexView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test']=None
        return TwitterTest.objects.filter(user=self.request.user)

class TwitterTestDetailView(generic.DetailView):
    model = TwitterTest
    context_object_name = 'test'
    template_name = 'twitter/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(TwitterTest, pk=pk)
            request.session['test']=test.id
        return super(TwitterTestDetailView,self).get(self, request, *args, **kwargs)

class TwitterTestDeleteView(DeleteView):
    model = TwitterTest
    template_name = 'confirm_delete.html'
    success_url = '/test/twitter/'

class TwitterTestCreateView(CreateView):
    model = TwitterTest
    template_name = 'twitter/list_modal.html'
    success_url = '/test/twitter/'
    form_class = TwitterTestForm
    page_title = 'Add a new twitter test'
    button_value = 'Add twitter test'
    item_type = 'twitter test'

    def get_context_data(self, **kwargs):
        context = super(TwitterTestCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['form_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class TwitterTestUpdateView(UpdateView):
    model = TwitterTest
    template_name = 'item.html'
    success_url = '/test/twitter/'
    form_class = TwitterTestForm
    page_title = 'Update twitter test details'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(TwitterTestUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

class TwitterTestSendTweetView(generic.View):
    success_url = '/test/twitter/'

    def get(self, request, *args, **kwargs):
        pk = request.session['test']
        org_pk = request.session['organisation']
        #twitter = get_object_or_404(TwitterTest, pk=pk)
        org = get_object_or_404(Organisation, pk=org_pk)
        targets = []


        #it = Twitter(auth=OAuth(token,  token_key, xconDNuSAn4dgwL8Lks15RgunqkfnTfVAo0Smejok4V023iuHG, ppIdalf76qTZdkmndPdsDA5Tg))

        people = Person.objects.filter(organisation=org)
        for p in people:
            identifiers = p.identifier_set.all()
            for i in identifiers:
                if i.identifiertype == Identifier.TWITTER:
                    targets.append("'"+i.identifier+"'")

        # currently sends to all people in organisation - this will need addressing

        #twitter = Twython(APP_KEY, APP_SECRET,
                 # OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        twitter = Twython('1JMWxaYJ6nwHPMdnr3Oga4exc', 'OFLD3aEvwgfdYyIvo1ql1pA8YSSzVPNhtd1wHrGahl988lbV2u',
                  '2981043486-0a3rXFy5mC99PMaKzPRy73F8uFQyVxVhUQnmAEO', 'DHVSBkipAOiyIW2ukHifAXM2E7ikFTSSyUuWS3ow5uSoz')

        twitter.update_status(status='Testing')

        return HttpResponseRedirect(reverse('emailtestindex'))