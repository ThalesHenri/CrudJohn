from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('cadastrarProdutos/', views.cadastrarProdutos, name='cadastrarProdutos'),

    path('mostrarProdutos/', views.mostrarProdutos, name='mostrarProdutos'),

    path('cadastrarProdutos/event/', views.cadastrarProdutosEvent, name='cadastrarProdutosEvent')
    
]