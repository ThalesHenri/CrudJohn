from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ProdutoForm

# Create your views here.

def home(response):
    return render(response,'index.html')


def cadastrarProdutos(response):
    form = ProdutoForm()
    context = {'form':form}
    return render(response,'cadastroProdutos.html', context)


def mostrarProdutos(response):
    return render(response,'mostrarProdutos.html')


def cadastrarProdutosEvent(response):
    if response.method == 'POST':
        form = ProdutoForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('sucess')
    return HttpResponse('failed')