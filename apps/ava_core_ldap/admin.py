from django.contrib import admin

# Register your models here.
from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup,QueryParameters

admin.site.register(ActiveDirectoryUser)
admin.site.register(ActiveDirectoryGroup)
admin.site.register(QueryParameters)
