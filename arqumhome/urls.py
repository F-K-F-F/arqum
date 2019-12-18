from django.urls import path
from arqumhome import views

urlpatterns = [
    path('', views.index, name='index'),
    path('altacliente', views.altacliente, name='altacliente'),
    path('bajacliente', views.bajacliente, name='bajacliente'),
    path('consultacliente', views.consultacliente, name='consultacliente'),
    #path('cargar_cliente', views.cargar_cliente, name='cargar_cliente'),
]
