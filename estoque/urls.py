from django.urls import path
from .import views

urlpatterns = [
    path('registrar-produto/', views.registrar_produto, name = "registrar_produto"),
    path('registrar-estoque/', views.registrar_produtoestoque, name = "registrar_estoque"),
    path('produto-estoque/', views.visualizar_produtoestoque, name = "produto_estoque"),
]