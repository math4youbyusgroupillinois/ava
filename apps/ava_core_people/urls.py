from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_people import views

urlpatterns = patterns('',
    
    #url(r'^$', login_required(views.PersonIndexView.as_view()), name='index'),
    #url(r'^(?P<pk>\d+)/$', login_required(views.PersonIndexView.as_view()), name='people'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.PersonDetailView.as_view()), name='people_view'),
    url(r'^new/$',login_required(views.PersonCreateView.as_view()),name='people_new'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.PersonUpdateView.as_view()), name='people_update'),
    url(r'^(?P<pk>\d+)/id/update/$', login_required(views.IdentifierUpdateView.as_view()), name='identifier_update'),
    url(r'^(?P<pk>\d+)/id/delete/$', login_required(views.IdentifierDeleteView.as_view()), name='identifier_delete'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.PersonDeleteView.as_view()), name='people_delete'),
)
