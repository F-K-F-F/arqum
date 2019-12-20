from django import forms
from .models import Cliente


class CargarForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'domicilio_real', 'domicilio_obra', 'correo',
                  'telefono', 'fecha_alta_cliente', 'fecha_inicio_obra', 'fecha_fin_obra')

        error_messages = {
            'nombre_cliente': {
                'required': ("El nombre del cliente es obligatorio"),
            },
            'domicilio_real': {
                'required': ("El domicilio real es obligatorio"),
            },
            'domicilio_obra': {
                'required': ("El domicilio de obra es obligatorio"),
            },
            'correo': {
                'required': ("Debe proporcionar correo electrónico"),
            },
            'fecha_alta_cliente': {
                'required': ("Debe informar la fecha de alta del cliente"),
            },
        }

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, *kwargs)
