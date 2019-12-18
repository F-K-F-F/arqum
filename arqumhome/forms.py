from django import forms
from .models import Cliente


class CargarForm(forms.Form):
    nombre_cliente = forms.CharField(
        label='Nombre del cliente:', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' 'input-50'}))
    domicilio_real = forms.CharField(
        label='Domicilio real:', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    domicilio_obra = forms.CharField(
        label='Domicilio de obra:', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.EmailField(
        label='Correo electrónico:', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(
        label='Teléfono:', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_alta_cliente = forms.DateField(
        label='Fecha de alta de cliente:', widget=forms.SelectDateWidget(years=range(2019, 2100), attrs={'class': 'form-control'}))
    fecha_inicio_obra = forms.DateField(
        label='Fecha de inicio de obra:', widget=forms.SelectDateWidget(years=range(2019, 2100), attrs={'class': 'form-control'}))
    fecha_fin_obra = forms.DateField(
        label='Fecha de alta de cliente:', widget=forms.SelectDateWidget(years=range(2019, 2100), attrs={'class': 'form-control'}))

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
