from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),

    path('cadastrarProdutos/', views.cadastrarProdutos, name='cadastrarProdutos'),

    path('mostrarProdutos/', views.mostrarProdutos, name='mostrarProdutos'),

    path('cadastrarProdutos/event/', views.cadastrarProdutosEvent, name='cadastrarProdutosEvent')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)