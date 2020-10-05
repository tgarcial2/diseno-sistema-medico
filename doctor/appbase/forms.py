from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    
        class Meta:
            model = Paciente
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(PacienteForm, self).__init__(*args,**kwargs)
            self.fields['foto'].widget.attrs['class'] = ' btn btn-warning btn-sm'
            self.fields['cedula'].widget.attrs['class'] = 'form-control'
            self.fields['cedula'].widget.attrs['placeholder'] = 'cedula'
            self.fields['nombre'].widget.attrs['class'] = 'form-control'
            self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese sus nombres'
            self.fields['apellido'].widget.attrs['class'] = 'form-control'
            self.fields['apellido'].widget.attrs['placeholder'] = 'Ingrese sus apellidos'
            self.fields['nacimiento'].widget.attrs['class']='form-control'
            self.fields['sexo'].widget.attrs['class']='form-control'
            self.fields['civil'].widget.attrs['class']='form-control'
            self.fields['profesion'].widget.attrs['class']='form-control'
            self.fields['titulo'].widget.attrs['class']='form-control'
            self.fields['provincia'].widget.attrs['class']='form-control'
            self.fields['ciudad'].widget.attrs['class']='form-control'
            self.fields['telefono'].widget.attrs['class']='form-control'
            self.fields['direccion'].widget.attrs['class']='form-control'
            self.fields['email'].widget.attrs['placeholder']='@example.com'
            self.fields['email'].widget.attrs['class']='form-control'
            self.fields['sangre'].widget.attrs['class']='form-control'
            self.fields['hijos'].widget.attrs['class']='form-control'
            
            
           