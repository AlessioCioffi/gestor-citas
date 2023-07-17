from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Solicitud
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


class Requests(LoginRequiredMixin, ListView):

    model = Solicitud
    template_name = 'solicitud/requests.html'
    context_object_name = 'solicitudes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:        
            context['solicitudes']= Solicitud.objects.all()
        else:
            context['solicitudes']=Solicitud.objects.filter(user=self.request.user)
        return context


class Request(LoginRequiredMixin, DetailView):
    model = Solicitud
    template_name = 'solicitud/request.html'
    context_object_name = 'solicitud'


class CreateRequest(CreateView):
    model = Solicitud
    template_name = 'solicitud/create_request.html'
    fields = ['name','surname','n_document','description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateRequest, self).form_valid(form)


class UpdateSolicitud(LoginRequiredMixin, UpdateView):
    model = Solicitud
    template_name = 'solicitud/update_request.html'
    fields = ['name','surname','n_document','type']
    template_name_suffix = '_update_form_'

    def get_success_url(self):
        return reverse_lazy('update_request',args=[self.object.id])+'?ok'


class DeleteSolicitud(LoginRequiredMixin, DeleteView):

    model = Solicitud
    template_name = 'solicitud/delete_request.html'
    success_url = reverse_lazy('requests')
    context_object_name = 'solicitudes'

