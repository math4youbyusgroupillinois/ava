from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_vis_graph import views

urlpatterns = patterns('',
    
    url(r'^ldap/(?P<pk>\d+)/$', login_required(views.LDAPGraphView.as_view()), name='ldap_graph_view'),
)
