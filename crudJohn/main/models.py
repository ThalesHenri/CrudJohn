from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    peso = models.DecimalField(max_digits=100, decimal_places=2)
    foto = models.ImageField(upload_to='media/', blank=True, null=True)
    def _str_(self):
        return self.nome
    
class Compras(models.Model):
    cliente = models.CharField(max_length=100)
    valorPago = models.DecimalField(max_digits=100, decimal_places=2)
    pagamento = models.BooleanField(default=True)
    produtosComprados = models.IntegerField()
    quantidadeProdutos = models.IntegerField()
    def _str_(self):
        texto = f"{self.cliente} >>{self.produto}"
        return texto

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)
    telefone = models.IntegerField(unique=True)
    def _str_(self):
        return self.nome