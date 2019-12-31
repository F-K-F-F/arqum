from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from arqumhome.models import Cliente
from arqumhome.forms import CargarForm, UsuarioForm, InfoPerfilUsuarioForm
from django.views.generic import View


def index(request):
    contenido = {'nombre_sitio': 'Arqum'}
    return render(request, 'arqumhome/index.html', contenido)


@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(''))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UsuarioForm(data=request.POST)
        profile_form = InfoPerfilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UsuarioForm()
        profile_form = InfoPerfilUsuarioForm
    return render(request, 'arqumhome/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            # else:
                # return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'arqumhome/login.html')


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


class FormularioDeBaja(View):
    template = 'arqumhome/bajacliente.html'
