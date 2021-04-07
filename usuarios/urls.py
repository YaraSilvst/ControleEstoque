from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registrar-pessoa/', views.registrar_pessoa, name = "registrar_pessoa"),
    path('registrar-gerente/', views.registrar_gerente, name = "registrar_gerente"),
    path('registrar-vendedor/', views.registrar_vendedor, name = "registrar_vendedor"),
    path('registrar-empresa/', views.registrar_empresa, name = "registrar_empresa"),
]
