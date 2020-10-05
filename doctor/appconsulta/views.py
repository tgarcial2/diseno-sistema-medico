from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class DoctorView(TemplateView):
    template_name = "appconsulta/doctor/doctor.html"

class HistoriaView(TemplateView):
    template_name = "appconsulta/historial/historia-clinica.html"

class CitaView(TemplateView):
    template_name = "appconsulta/atencion/cita.html"

class AgendaView(TemplateView):
    template_name = "appconsulta/agenda/agenda-consulta.html"

class HorarioView(TemplateView):
    template_name = "appconsulta/configuracion/horario.html"

class RecetaView(TemplateView):
    template_name = "appconsulta/configuracion/receta.html"

class AntecedentesView(TemplateView):
    template_name = "appconsulta/configuracion/antecedentes.html"

class UsuarioView(TemplateView):
    template_name = "inicio-login/usuario.html"