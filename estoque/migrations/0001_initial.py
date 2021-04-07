# Generated by Django 3.0 on 2021-04-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_tipo', models.CharField(choices=[('PERECIVEl', 'Perecível'), ('NÃO PERECIVEL', 'Não Perecível')], max_length=50, verbose_name='Tipo')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=194, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'produtos',
                'db_table': 'produto',
            },
        ),
        migrations.CreateModel(
            name='ProdutoEstoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, max_length=50, verbose_name='Quantidade')),
                ('data_validade', models.DateField(max_length=50, verbose_name='Data Validade')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto', verbose_name='Produto')),
            ],
        ),
    ]
