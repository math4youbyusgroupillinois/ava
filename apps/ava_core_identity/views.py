from django.shortcuts import render


class IdentityDeleteView(DeleteView):
    model = Identity
    template_name = 'confirm_delete.html'
    success_url = '/'


class IdentityCreateView(CreateView):
    model = Identity
    template_name = 'item.html'
    success_url = '/'
    form_class = IdentityForm
    page_title = 'add'
    button_value = 'add'
    item_type = 'identity'

    def get_context_data(self, **kwargs):
        context = super(IdentityCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        context['item_type'] = self.item_type
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class IdentityUpdateView(UpdateView):
    model = Identity
    template_name = 'item.html'
    success_url = '/'
    form_class = IdentityForm
    page_title = 'update'
    button_value = 'update'
    item_type = 'identity'

    def get_context_data(self, **kwargs):
        context = super(IdentityUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        context['item_type'] = self.item_type
        return context


#class IdentityDetailView(DetailView):
#    model = Identity
#    template_name = 'identity/view.html'


class IdentityIndexView(ListView):
    model = Identity
    template_name = 'identity/index.html'
