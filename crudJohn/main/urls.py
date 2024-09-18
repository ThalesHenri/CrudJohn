from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),


    path('cadastrarProdutos/', views.cadastrarProdutos, name='cadastrarProdutos'),


    path('mostrarProdutos/', views.mostrarProdutos, name='mostrarProdutos'),


    path('cadastrarProdutos/event/', views.cadastrarProdutosEvent, name='cadastrarProdutosEvent'),


    path('cadastrarClientes/', views.cadastrarClientes, name="cadastrarClientes" ),


    path('mostrarClientes/', views.mostrarClientes, name='mostrarClientes'),


    path('cadastrarClientes/event/', views.cadastrarClientesEvent, name='cadastrarClientesEvent'),


   path('cadastrarCompras/', views.cadastrarCompras, name='cadastrarCompras'),


    path('mostrarCompras/', views.mostrarCompras, name='mostrarCompras'),


    path('cadastrarCompras/event/', views.cadastrarComprasEvent, name='cadastrarComprasEvent'),


    path('marcar-pagamento/<int:id>/', views.marcar_pagamento, name='marcar_pagamento'),
        
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)