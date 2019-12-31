from django import forms
from .models import Cliente, InfoPerfilUsuario
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class InfoPerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoPerfilUsuario
        fields = ('foto_perfil', )


class CargarForm(forms.Form):

    nombre_cliente = forms.CharField(
        label='Nombre del cliente',
        max_length=200)

    domicilio_real = forms.CharField(
        label='Domicilio real',
        max_length=200
    )

    domicilio_obra = forms.CharField(
        label='Domicilio de obra',
        max_length=200
    )

    correo = forms.EmailField(
        label='Correo electrónico',
        max_length=254
    )

    telefono = forms.CharField(
        label='Teléfono de contacto',
        max_length=200,
        required=False
    )

    fecha_alta_cliente = forms.DateField(
        label='Fecha de alta de cliente',
    )

    fecha_inicio_obra = forms.CharField(
        label='Fecha de inicio de obra',
        max_length=8,
        required=False
    )

    fecha_fin_obra = forms.CharField(
        label='Fecha de fin de obra',
        # max_length=10,
        required=False
    )

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
