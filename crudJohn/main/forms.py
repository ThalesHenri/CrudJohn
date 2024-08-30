from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco', 'peso', 'foto']
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),

            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade do Produto'}),

            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),

            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}),

            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'})

                   }
