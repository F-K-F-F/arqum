from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from arqumhome.models import Cliente
from arqumhome.forms import CargarForm
from django.views.generic import View


def index(request):
    contenido = {'nombre_sitio': 'Arqum'}
    return render(request, 'arqumhome/index.html', contenido)


def altacliente(request):
    return render(request, 'arqumhome/altacliente.html')


def bajacliente(request):
    return render(request, 'arqumhome/bajacliente.html')


def consultacliente(request):
    return render(request, 'arqumhome/consultacliente.html')


class FormularioDeAlta(View):
    template = 'arqumhome/altacliente.html'

    def get(self, request):

        form = CargarForm()
        params = {}
        prueba = "dato de prueba"
        params['prueba'] = prueba
        params['form'] = form
        return render(request, self.template, params)

    def post(self, request):

        # if request.method == 'POST':
        #form = CargarForm(request.POST)

        if request.method == 'POST':
            form = CargarForm(request.POST)
            if form.is_valid():
                try:
                    nombre_cliente = form.cleaned_data['nombre_cliente']
                    domicilio_real = form.cleaned_data['domicilio_real']
                    domicilio_obra = form.cleaned_data['domicilio_obra']
                    correo = form.cleaned_data['correo']
                    telefono = form.cleaned_data['telefono']
                    fecha_alta_cliente = form.cleaned_data['fecha_alta_cliente']
                    fecha_inicio_obra = form.cleaned_data['fecha_inicio_obra']
                    fecha_fin_obra = form.cleaned_data['fecha_fin_obra']

                    newcliente = Cliente(nombre_cliente=nombre_cliente, domicilio_real=domicilio_real, domicilio_obra=domicilio_obra, correo=correo,
                                         telefono=telefono, fecha_alta_cliente=fecha_alta_cliente, fecha_inicio_obra=fecha_inicio_obra, fecha_fin_obra=fecha_fin_obra)
                    newcliente.save()
                    return redirect('index')
                except:
                    pass
        else:
            form = CargarForm()

        # return render(request, 'arqumhome/altacliente.html', {'form': form})
