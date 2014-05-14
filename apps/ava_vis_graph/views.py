from django.shortcuts import render
from django.views import generic
from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup, QueryParameters


class LDAPGraphView(generic.ListView):
    template_name = 'graph/ldap.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        results = QueryParameters.objects.filter(pk=1)
        exp = ExportLDAP()
        for qp in results :
            nodes = exp.nodes(self,qp)
        return ActiveDirectoryUser.objects.filter(user=self.request.user)


class ExportLDAP():
    nodes = []
    edges = []

    def nodes(self, parameters):
        ldap_users = ActiveDirectoryUser.objects.filter(queryparameters=parameters,user=self.request.user)
        for user in ldap_users:
            nodes.append(self.model_to_dict(user))
        print nodes
        ldap_groups = ActiveDirectoryGroup.objects.filter(queryparameters=parameters,user=self.request.user)
        for group in ldap_groups:
            nodes.append(self.model_to_dict(group))
        print nodes
        return nodes


    def edges(self, parameters):
        pass

    def model_to_dict(instance, fields=None, exclude=None):
        """
        Returns a dict containing the data in ``instance`` suitable for passing as
        a Form's ``initial`` keyword argument.
    
        ``fields`` is an optional list of field names. If provided, only the named
        fields will be included in the returned dict.
    
        ``exclude`` is an optional list of field names. If provided, the named
        fields will be excluded from the returned dict, even if they are listed in
        the ``fields`` argument.
        """
        # avoid a circular import
        from django.db.models.fields.related import ManyToManyField
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.virtual_fields + opts.many_to_many:
            if not getattr(f, 'editable', False):
                continue
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                # If the object doesn't have a primary key yet, just use an empty
                # list for its m2m fields. Calling f.value_from_object will raise
                # an exception.
                if instance.pk is None:
                    data[f.name] = []
                else:
                    # MultipleChoiceWidget needs a list of pks, not object instances.
                    qs = f.value_from_object(instance)
                    if qs._result_cache is not None:
                        data[f.name] = [item.pk for item in qs]
                    else:
                        data[f.name] = list(qs.values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data
