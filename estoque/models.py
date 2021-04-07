from django.db import models
from usuarios.models import *

STATUS_TIPO = [
    ("PERECIVEl", "Perecível"),
    ("NÃO PERECIVEL", "Não Perecível"),
]

class Produto(models.Model):

    status_tipo = models.CharField(
        verbose_name = "Tipo",
        max_length = 50,
        choices = STATUS_TIPO,
    )
    
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 194,
    )

    descricao = models.CharField(
        verbose_name = "Descrição",
        max_length = 194,
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "produtos"
        db_table = "produto"

    def __str__(self):
        return self.nome


class ProdutoEstoque(models.Model):

    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, verbose_name="Produto")

    quantidade = models.FloatField(
        verbose_name = "Quantidade",
        default=0,  
    )

    data_validade = models.DateField(
        verbose_name = "Data Validade",
        max_length = 50,
        auto_now = False,
        auto_now_add = False,
    )

    class Meta:
        verbose_name = "Produto Estoque"
        verbose_name_plural = "Produtos Estoque"
        db_table = "produtoestoque"

    def __str__(self):
        return self.produto.nome

    



