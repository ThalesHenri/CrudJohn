from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco', 'peso', 'foto']
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 
                                           'placeholder': 'Nome do Produto',
                                           'style': 'font-family: verdana, sans-serif;'}),

            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 
                                                   'placeholder': 'Quantidade do Produto',
                                                   'style': 'font-family: verdana, sans-serif;'}),

            'preco': forms.NumberInput(attrs={'class': 'form-control', 
                                              'placeholder': 'R$',
                                              'style': 'font-family: verdana, sans-serif;'}),

            'peso': forms.NumberInput(attrs={'class': 'form-control', 
                                             'placeholder': 'Kg',
                                             'style': 'font-family: verdana, sans-serif;'}),

            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'})

                   }
