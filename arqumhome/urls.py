from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from arqumhome import views


urlpatterns = [
    path('index', views.index, name='index'),
    # path('admin', admin.site.urls),
    path('altacliente', views.altacliente, name='altacliente'),
    path('bajacliente', views.bajacliente, name='bajacliente'),
    path('consultacliente', views.consultacliente, name='consultacliente'),
    path('buscacliente', views.buscacliente, name='buscacliente'),
    path('cargar_cliente', views.FormularioDeAlta.as_view(), name='cargar'),
    path('bajar_cliente', views.FormularioDeBaja.as_view(), name='bajar'),
    path('consultar_cliente', views.FormularioDeConsulta.as_view(), name='consultar'),
    path('special', views.special, name='special'),
    path('user_logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('', views.user_login, name='user_login'),
]
