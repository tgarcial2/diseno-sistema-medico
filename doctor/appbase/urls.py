from django.contrib import admin
from django.urls import path
from appbase.views import CreatePacienteView, UpdatePacienteView,ListPacienteView
from django.conf import settings
app_name = "base"
urlpatterns = [
    path('paciente/', ListPacienteView.as_view(), name='paciente'),
    path('paciente_registro/', CreatePacienteView.as_view(), name='pac_r'),
    path('paciente_actualizar/<int:pk>/', UpdatePacienteView.as_view(), name='act_paciente'),
]
