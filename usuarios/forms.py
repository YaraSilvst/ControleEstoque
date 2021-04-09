from django import forms
from usuarios.models import *

class PessoaForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
    class Meta: 
        model = Pessoa
        fields = [
            "nome_completo", "cpf", "data_nascimento", "email", "celular", "password"
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo do usuário é obrigatório para o registro",
            },

            "cpf": {
                "required": "O cpf do usuário é obrigatório para o registro",
            },

            "data_nascimento": {
                "required": "A data de nascimento do usuário é obrigatória para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)",
            },

            "email": {
                "required": "O email do usuário é obrigatória para o registro",
            },

            "celular": {
                "required": "O celular do usuário é obrigatória para o registro",
            },
            "password": {
                "required": "Insira uma senha válida",
            },
        }

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ("__all__")


class EmpresaForm(forms.ModelForm):
    class Meta: 
        model = Empresa
        fields = [
            "nome_empresa", "telefone","estado", "cidade",
        ]

        error_messages = {
            "nome_empresa": {
                "required": "O nome da empresa é obrigatória para o registro",
            },

            "telefone": {
                "required": "O telefone da empresa é obrigatório para o registro",
            },     
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ("__all__")
