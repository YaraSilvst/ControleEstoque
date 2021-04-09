from django.urls import path
from .import views

urlpatterns = [
    path('produto-movimentacaoentrada/', views.movimentacaoentrada, name = "movimentacao_entrada"),
    path('produto-movimentacaosaida/', views.movimentacaosaida, name = "movimentacao_saida"),
    path('relatorio/', views.relatorio, name = "relatorio"),
]