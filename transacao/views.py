from django.shortcuts import render, redirect
from django.contrib import messages
from transacao.models import *
from transacao.forms import *

def movimentacaosaida(request):

    form = MovimentacaoForm()
    listProdutos = ProdutoEstoque.objects.filter(quantidade__gt=0)

    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        
        if form.is_valid():
            movimentacao = form.save(commit=False)
            objMovimentacao = form.save(commit=False)
            objMovimentacao.status_movimentacao = 'SAI'
            objMovimentacao.save()

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

                if movimentacao.status_movimentacao == "SAI":
                    objProdutoEstoque.quantidade -= float(objProdutoMovi.quantidade)

                objProdutoEstoque.save()
            messages.success(request, "Movimentação registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Movimentação",
        "form": form,
        "listProdutos":listProdutos,
    }

    return render(request, "movimentacao_saida.html", context)


def movimentacaoentrada(request):

    form = MovimentacaoForm()
    listProdutos = Produto.objects.all()

    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        
        if form.is_valid():
            objMovimentacao = form.save(commit=False)
            objMovimentacao.status_movimentacao = 'ENT'
            objMovimentacao.save()

            listProdutosMovi = request.POST.getlist("Produto[]", None)
            listQtdMovi = request.POST.getlist("Qtd[]", None)
            listDataValiMovi = request.POST.getlist("DataVali[]", None)

            for index, q in enumerate(listProdutosMovi):

                objProduto = Produto.objects.get(pk=listProdutosMovi[index])

                objProdutoEstoque = ProdutoEstoque ()                
                objProdutoEstoque.produto = objProduto              
                objProdutoEstoque.quantidade = listQtdMovi[index]
                objProdutoEstoque.data_validade = listDataValiMovi[index]
                objProdutoEstoque.save()

                objProdutoMovi = ProdutoMovimentacao()
                objProdutoMovi.movimentacao = objMovimentacao
                objProdutoMovi.produto = objProduto
                objProdutoMovi.quantidade = listQtdMovi[index]
                objProdutoMovi.save()

            messages.success(request, "Movimentação registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Movimentação",
        "form": form,
        "listProdutos":listProdutos,
    }

    return render(request, "movimentacao_entrada.html", context)


def relatorio(request):

    listMovi = Movimentacao.objects.all().order_by("-pk")
    listrelatorio = []
    for q in listMovi:
        listProdutoMovi = ProdutoMovimentacao.objects.filter(movimentacao=q)
        
        obj = {
            'Movimentacao':q,
            'Produtos':listProdutoMovi,
        }
        listrelatorio.append(obj)

    context = {
        "nome_pagina": "Relatorio",
        "listrelatorio":listrelatorio,
    }

    return render(request, "relatorio.html", context)


    




