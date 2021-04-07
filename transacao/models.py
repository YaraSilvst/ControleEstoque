from django.db import models
from usuarios.models import *
from estoque.models import *

STATUS_MOVIMENTACAO = [
    ("ENT", "Entrada"),
    ("SAI", "Saída"),
]

class Movimentacao(models.Model):

    status_movimentacao = models.CharField(
        verbose_name = "Movimentação",
        max_length = 50,
        choices = STATUS_MOVIMENTACAO,
    )

    data = models.DateField(
        verbose_name = "Data Movimentação",
        max_length = 50,
        auto_now_add = True,
    )

    gerente = models.ForeignKey(Gerente, on_delete = models.CASCADE, verbose_name="Gerente")

    vendedor = models.ForeignKey(Vendedor, on_delete = models.CASCADE, verbose_name="Vendedor")

    empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, verbose_name="Empresa")

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "movimentações"
        db_table = "movimentacao"

    def __str__(self):
        return self.status_movimentacao

class ProdutoMovimentacao(models.Model):

    movimentacao = models.ForeignKey(Movimentacao, on_delete = models.CASCADE, verbose_name="Movimentação")

    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, verbose_name="Produto")

    quantidade = models.FloatField(verbose_name="Quantidade",default=0)


    class Meta:
        verbose_name = "Movimentação do Produto"
        verbose_name_plural = "Movimentações dos Produtos"
        db_table = "produtomovimentacao"

    def __str__(self):
        return self.produto.nome



    





