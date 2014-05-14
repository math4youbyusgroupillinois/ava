from django.shortcuts import render
from django.views import generic
from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup, QueryParameters


class LDAPGraphView(generic.DetailView):
    template_name = 'graph/ldap.html'

    def get_context_data(self, **kwargs):
        context = super(LDAPGraphView, self).get_context_data(**kwargs)
        exp = ExportLDAP()
        for qp in results :
            contex['json'] = exp.nodes(qp)
        return context

class ExportLDAP():
    edges = []

    def nodes(self, parameters):
        nodes = []
        index = {}
        json = "{\"nodes\":"
        ldap_users = ActiveDirectoryUser.objects.filter(queryParameters=parameters)
        for user in ldap_users:
            index[user.id] = user
            #print user.memberOf.all()
            nodes.append(self.model_to_dict(user))
        #print index
        user_count = len(index)
        #print nodes
        ldap_groups = ActiveDirectoryGroup.objects.filter(queryParameters=parameters)
        for group in ldap_groups:
            nodes.append(self.model_to_dict(group))
            pointer = group.id+user_count
            index[pointer] = group
            #index.append("GROUP::"+group.id)
        #print index
        edges = []
        
        for key,value in index.iteritems():
             if isinstance(value,ActiveDirectoryGroup):
                 users = value.member.all()
                 #print groups
                 for user in users:
                     #print user
                     e = {}
                     e['value'] = 'edge'+str(user.id)+"_"+key
                     e['source'] = user.id-1
                     e['target'] = key-1
                     edges.append(e)
        json = json + str(nodes)+ ", \"links\":"+str(edges) + "}"
        print json        #self.edges(parameters,nodes,index)
        return json


    def edges(self, parameters,nodes,index):
        edges = []
        for i in index:
            pass    

    def model_to_dict(self,instance, fields=None, exclude=None):
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
