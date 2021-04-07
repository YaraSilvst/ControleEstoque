from django.shortcuts import render, redirect
from django.contrib import messages
from estoque.models import *
from estoque.forms import *

def registrar_produto(request):

    form = ProdutoForm()

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)

            produto.save()

            messages.success(request, "Produto registrado com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Produto",
        "form": form
    }

    return render(request, "registrar_produto.html", context)



def registrar_produtoestoque(request):

    form = ProdutoEstoqueForm()

    if request.method == "POST":
        form = ProdutoEstoqueForm(request.POST)

        if form.is_valid():
            produtoestoque = form.save(commit=False)

            produtoestoque.save()

            messages.success(request, "Produto Estoque registrado com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Produto Estoque",
        "form": form
    }

    return render(request, "registrar_estoque.html", context)


