from django import forms
from .models import Solicitud, Cliente

class ConfirmarSolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['estado_actual']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
