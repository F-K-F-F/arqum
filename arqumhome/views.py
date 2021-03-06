from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, FormView
from django.views import View
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Cliente
from arqumhome.forms import CargarForm, UsuarioForm, InfoPerfilUsuarioForm, BajarForm, SearchForm


def index(request):
    contenido = {'nombre_sitio': 'Arqum'}
    return render(request, 'arqumhome/index.html', contenido)


# USUARIOS #

@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        profile_form = InfoPerfilUsuarioForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['foto_perfil']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UsuarioForm()
        profile_form = InfoPerfilUsuarioForm()
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
                return redirect(reverse('index'))
            # else:
                # return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'arqumhome/login.html')

# -------------------- #

# RENDER DE PLANTILLAS #


@login_required(login_url='user_login')
def altacliente(request):
    return render(request, 'arqumhome/altacliente.html')


@login_required
def bajacliente(request):
    return render(request, 'arqumhome/bajacliente.html')


@login_required
def consultacliente(request):
    return render(request, 'arqumhome/consultacliente.html')


@login_required(login_url='user_login')
def buscacliente(request):
    return render(request, 'arqumhome/buscacliente.html')
# --------------------- #

# CLASES PARA EL MODELO #


class FormularioDeAlta(View):
    template = 'arqumhome/altacliente.html'

    @login_required
    def get(self, request):

        form = CargarForm()
        params = {}
        prueba = "dato de prueba"
        params['prueba'] = prueba
        params['form'] = form
        return render(request, self.template, params)

    @login_required
    def post(self, request):

        # if request.method == 'POST':
        # form = CargarForm(request.POST)

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

    def get(self, request):
        form = BajarForm()
        params = {}
        prueba = "dato de prueba"
        params['prueba'] = prueba
        params['form'] = form
        return render(request, self.template, params)

    def post(self, request):
        if request.method == 'POST':
            form = BajarForm(request.POST)
            if form.is_valid:
                try:
                    obj = get_object_or_404(Cliente)
                    obj.delete()
                except:
                    pass
        else:
            form = BajarForm()
        return render(request, 'arqumhome/bajacliente.html', {'form': form})


class FormularioDeConsulta(ListView):
    model = Cliente

    template_name = 'arqumhome/buscacliente.html'
    form_class = SearchForm

    def get_queryset(self):
        try:
            query = self.request.GET.get('q')
            object_list = Cliente.objects.filter(
                Q(nombre_cliente__icontains=query) | Q(
                    domicilio_obra__icontains=query)
            )
            return object_list
        except:
            HttpResponse('No existe el cliente')


# --------------------- #
