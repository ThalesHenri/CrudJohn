from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ProdutoForm
from .models import Produto


def home(response):
    return render(response,'index.html')


def cadastrarProdutos(response):
    form = ProdutoForm()
    context = {'form':form}
    return render(response,'cadastroProdutos.html', context)


def mostrarProdutos(response):
    produto = Produto.objects.all()
    context = {'produtos': produto}
    return render(response, 'mostrarProdutos.html', context)


def cadastrarProdutosEvent(response):
    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES)
        if form.is_valid():
            produto = form.save()
            print(f'o caminho da foto é:{produto.foto}')
            return HttpResponse('sucess')
    return HttpResponse('failed')