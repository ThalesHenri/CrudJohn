from django.shortcuts import render,  HttpResponse, get_object_or_404, redirect
from .forms import ProdutoForm, ClienteForm, ComprasForm
from .models import Produto, Cliente, Compras


def home(response):
    return render(response,'index.html')


def cadastrarProdutos(response):
    form = ProdutoForm()
    context = {'form':form}
    return render(response,'cadastroProdutos.html', context)

 
def cadastrarClientes(response):
    form = ClienteForm()
    context = {'form': form}
    return render(response, 'cadastroCliente.html', context)


def cadastrarCompras(response):
    form = ComprasForm()
    context = {'form': form}
    return render(response, 'cadastroCompras.html', context)


def mostrarProdutos(response):
    produto = Produto.objects.all()
    context = {'mostrarProdutos': produto}
    return render(response, 'mostrarProdutos.html', context)


def mostrarClientes(response):
    cliente = Cliente.objects.all()
    context = {'mostrarClientes': cliente}
    return render(response, 'mostrarClientes.html', context)


def mostrarCompras(response):
    compras = Compras.objects.all()
    context = {'mostrarCompras': compras}
    return render(response, 'mostrarCompras.html', context)


def cadastrarProdutosEvent(response):
    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES)
        if form.is_valid():
            produto = form.save()
            return HttpResponse('Produto cadastrado com sucesso!')
    return HttpResponse('failed')


def cadastrarClientesEvent(response):
    if response.method == 'POST':
        form = ClienteForm(response.POST)
        if form.is_valid():
            cliente = form.save()
            return HttpResponse('Cliente cadastrado com sucesso!')
    return HttpResponse('failed')


def cadastrarComprasEvent(response):
    if response.method == 'POST':
        form = ComprasForm(response.POST)
        if form.is_valid():
            compras = form.save()
            return HttpResponse('Compra cadastrada com sucesso!')
    return HttpResponse('failed')


def marcar_pagamento(response, id):
    compra = get_object_or_404(Compras, pk=id)
    compra.pagamento = True
    compra.save()
    return redirect('/mostrarCompras/')