from django.urls import path
from .import views

urlpatterns = [
    path('movimentacao/', views.movimentacao, name = "movimentacao"),
    path('produto-movimentacao/<int:id_movimentacao>', views.produtomovimentacao, name = "produto_movimentacao"),
]