import json
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup, QueryParameters


class LDAPGraphView(generic.DeleteView):
    template_name = 'graph/ldap.html'
    model = QueryParameters

    def get_context_data(self, **kwargs):
        context = super(LDAPGraphView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            parameters = get_object_or_404(QueryParameters, pk=pk)
            exp = ExportLDAP()
            context['json'] = exp.nodes(parameters,False)
            context['link'] = "/graph/ldap/"+pk+"/hide/"
            context['link_message'] = "Hide Empty Groups"
        return context

class LDAPGraphHideView(generic.DeleteView):
    template_name = 'graph/ldap.html'
    model = QueryParameters

    def get_context_data(self, **kwargs):
        context = super(LDAPGraphHideView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            parameters = get_object_or_404(QueryParameters, pk=pk)
            exp = ExportLDAP()
            context['json'] = exp.nodes(parameters,True)
            context['link'] = "/graph/ldap/"+pk+"/"
            context['link_message'] = "Show Empty Groups"
        return context

class ExportLDAP():
    edges = []

    def nodes(self, parameters,hide):
        nodes = []
        elements = []
        ldap_users = ActiveDirectoryUser.objects.filter(queryParameters=parameters)
        fields=['displayName']
        for user in ldap_users:
            elements.append(user)
            current = self.model_to_dict(user,fields)
            current['node_type'] = 'user'
            nodes.append(current)
        #print index
        user_count = len(elements)
        #print nodes
        ldap_groups = ActiveDirectoryGroup.objects.filter(queryParameters=parameters)
        g = ['cn','member']
        for group in ldap_groups:
                current = self.model_to_dict(group,g)
                current['node_type'] = 'group'
                if(hide == True and group.member.count() > 0):
                    nodes.append(current)
                    elements.append(group)
                else:
                    if(hide == False):
                        nodes.append(current)
                        elements.append(group)
              
        edges = []
        
        #for key,value in index.iteritems():
        for index, value in enumerate(nodes):
            print value
            if isinstance(value,ActiveDirectoryGroup):
                 users = value.member.all()
                 print users
                 for user in users:
                     print user
                     e = {}
                     e['value'] = 'edge'+str(user.id)+"_"+str(key)
                     e['source'] = elements.index(user)
                     e['target'] = index
                     print e
                     edges.append(e)
        #json = "{\\\"nodes\\\":" + str(nodes)+ ", \\\"links\\\":"+str(edges) + "}"
        json_object = {}
        json_object['nodes'] = nodes;
        json_object['links'] = edges;
        j_out = json.dumps(json_object)
        #j_out = j_out + json.dumps(edges)
        #print j_out        #self.edges(parameters,nodes,index)
        return j_out


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
