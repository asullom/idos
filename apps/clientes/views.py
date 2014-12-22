from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Cliente
from .forms import ClienteForm


class ClienteDeleteView(generic.edit.BaseDeleteView):

    """ """
    model = Cliente
    success_url = reverse_lazy('cliente-index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ClienteUpdateView(generic.edit.UpdateView):

    """ """
    model = Cliente
    success_url = reverse_lazy('cliente-index')
    form_class = ClienteForm


class ClienteCreateView(generic.edit.CreateView):

    """ """
    model = Cliente
    success_url = reverse_lazy('cliente-index')
    form_class = ClienteForm


class ClienteListView(generic.ListView):

    """ Lista los clientes """
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['msg'] = 'hola django'

        return context
