from django import forms
from transacao.models import *

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        exclude = ["status_movimentacao"]
        fields = ("__all__")

class ProdutoMovimentacaoForm(forms.ModelForm):
    class Meta:
        model = ProdutoMovimentacao
        fields = ("__all__")
