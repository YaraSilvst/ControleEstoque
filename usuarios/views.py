from django.shortcuts import render, redirect
from django.contrib import messages
from estoque.models import *
from usuarios.models import *
from usuarios.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    listaprodutos = Produto.objects.all()
    context = {
        "listaprodutos": listaprodutos,
    }

    return render(request, "index.html", context)

def registrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit=False)

            pessoa.save()

            messages.success(request, "Usuário registrado com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Usuário",
        "form": form
    }

    return render(request, "registrar_pessoa.html", context)


@login_required
def registrar_gerente(request):

    form = GerenteForm()

    if request.method == "POST":
        form = GerenteForm(request.POST)

        if form.is_valid():
            gerente = form.save(commit=False)

            gerente.save()

            messages.success(request, "Gerente registrado com sucesso.")

            return redirect("index")
    
    context = {
        "nome_pagina": "Registrar Gerente",
        "form": form
    }

    return render(request, "registrar_gerente.html", context)


@login_required
def registrar_empresa(request):

    form = EmpresaForm()

    if request.method == "POST":
        form = EmpresaForm(request.POST)

        if form.is_valid():
            empresa = form.save()

            empresa.save()

            messages.success(request, "Empresa registrada com sucesso.")

            return redirect("index")
    
    context = {
        "nome_pagina": "Registrar Empresa",
        "form": form
    }

    return render(request, "registrar_empresa.html", context)


@login_required
def registrar_vendedor(request):

    form = VendedorForm()

    if request.method == "POST":
        form = VendedorForm(request.POST)

        if form.is_valid():
            vendedor = form.save(commit=False)

            vendedor.save()

            messages.success(request, "Vendedor registrado com sucesso.")

            return redirect("index")
    
    context = {
        "nome_pagina": "Registrar Vendedor",
        "form": form
    }

    return render(request, "registrar_vendedor.html", context)

