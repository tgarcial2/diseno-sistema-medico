from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm


class InicioView(TemplateView):
    template_name = "index.html"

class InicioLoginView(TemplateView):
    template_name = "inicio-login/login.html"

class RegistroLoginView(TemplateView):
    template_name = "inicio-login/registrar.html"

class ListPacienteView(ListView):
    model = Paciente
    template_name = "appbase/paciente/paciente.html"
    context_object_name = "pacientes"

class CreatePacienteView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "appbase/paciente/registro.html"
    success_url = reverse_lazy('base:paciente')
    form_valid_message = 'Datos Guardados'
    form_invalid_message = 'Error'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['POST'] = True
        return context

class UpdatePacienteView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "appbase/paciente/registro.html"
    success_url = reverse_lazy('base:paciente')
