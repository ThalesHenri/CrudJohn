# Generated by Django 5.1 on 2024-09-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_produto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='quantidadeProdutos',
            field=models.IntegerField(default=1),
        ),
    ]
