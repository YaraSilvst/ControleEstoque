from django import forms
from estoque.models import *

class ProdutoForm(forms.ModelForm):
    class Meta: 
        model = Produto
        fields = ("__all__")

        error_messages = {
            "nome": {
                "required": "O nome do produto é obrigatório para o registro"
            },
        }

class ProdutoEstoqueForm(forms.ModelForm):
    class Meta:
        model = ProdutoEstoque
        fields = [
            "produto", "quantidade", "data_validade",
        ]
