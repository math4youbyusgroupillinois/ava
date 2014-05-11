from django.conf.urls import patterns, include, url
from django.contrib import admin
from dh5bp.urls import urlpatterns as dh5bp_urls
from django.contrib.auth.decorators import login_required
from ava_core_project.views import DashboardView

admin.autodiscover()

handler404 = 'dh5bp.views.page_not_found'
handler500 = 'dh5bp.views.server_error'

urlpatterns = patterns('',
    url(r'^$', login_required(DashboardView.as_view()), name='index'),
    url(r'^ava/', include('ava_core.urls')),
    url(r'^accounts/', include('ava_core_auth.urls')),
    url(r'^project/', include('ava_core_project.urls')),
    url(r'^ldap/', include('module_activedirectory.urls')),
    url(r'^people/', include('ava_core_people.urls')),
    url(r'^org/', include('ava_core_org.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += dh5bp_urls
