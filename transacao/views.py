from django.shortcuts import render, redirect
from django.contrib import messages
from transacao.models import *
from transacao.forms import *

def movimentacao(request):

    form = MovimentacaoForm()
    listProdutos = ProdutoEstoque.objects.filter(quantidade__gt=0)
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        

        if form.is_valid():
            movimentacao = form.save(commit=False)

            movimentacao.save()
            listProdutosMovi = request.POST.getlist("Produto[]", None)
            listQtdMovi = request.POST.getlist("Qtd[]", None)

            for index, q in enumerate(listProdutosMovi):

                objProdutoEstoque = ProdutoEstoque.objects.get(pk=listProdutosMovi[index])                

                objProdutoMovi = ProdutoMovimentacao()                
                objProdutoMovi.movimentacao = movimentacao               
                objProdutoMovi.produto = objProdutoEstoque.produto
                objProdutoMovi.quantidade = listQtdMovi[index]
                objProdutoMovi.save()

                if movimentacao.status_movimentacao == "ENT":
                    objProdutoEstoque.quantidade += float(objProdutoMovi.quantidade)
                else:
                    objProdutoEstoque.quantidade -= float(objProdutoMovi.quantidade)

                objProdutoEstoque.save()
            messages.success(request, "Movimentação registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Movimentação",
        "form": form,
        "listProdutos":listProdutos,
    }

    return render(request, "movimentacao.html", context)


def produtomovimentacao(request, id_movimentacao):

    movimentacao = Movimentacao.objects.get(pk=id_movimentacao)

    form = ProdutoMovimentacaoForm()

    if request.method == "POST":
        form = ProdutoMovimentacaoForm(request.POST)

        if form.is_valid():
            produtomovimentacao = form.save(commit=False)

            produtomovimentacao.save()

            messages.success(request, "Produto Movimentação registrado com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Produto Movimentação",
        "form": form,
        "movimentacao": movimentacao,
    }

    return render(request, "produto_movimentacao.html", context)


