from django import forms
from transacao.models import *

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ("__all__")

class ProdutoMovimentacaoForm(forms.ModelForm):
    class Meta:
        model = ProdutoMovimentacao
        exclude = ["movimentacao"]
        fields = ("__all__")
