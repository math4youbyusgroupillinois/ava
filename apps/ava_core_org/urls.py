from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_org import views

urlpatterns = patterns('',
    
    url(r'^(?P<pk>\d+)/view/$', login_required(views.OrganisationDetailView.as_view()), name='org_view'),
    url(r'^new/$',login_required(views.OrganisationCreateView.as_view()),name='org_new'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.OrganisationUpdateView.as_view()), name='org_update'),
    url(r'^chart/$', login_required(views.OrganisationUnitUpdateView.as_view()), name='org_unit_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.OrganisationDeleteView.as_view()), name='org_delete'),
)
