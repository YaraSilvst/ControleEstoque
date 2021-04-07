# Generated by Django 3.0 on 2021-04-05 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=150, verbose_name='Nome Empresa')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('cep', models.CharField(max_length=14, verbose_name='CEP')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'empresas',
                'db_table': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('email', models.CharField(max_length=194, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('status_genero', models.CharField(choices=[('FEMININO', 'Feminino'), ('MASCULINO', 'Masculino'), ('OUTROS', 'Outros')], max_length=20, verbose_name='Sexo')),
                ('naturalidade', models.CharField(max_length=50, verbose_name='Naturalidade')),
                ('status_escolaridade', models.CharField(choices=[('EFI', 'Ensino Fundamental incompleto'), ('EFC', 'Ensino Fundamental completo'), ('EMI', 'Ensino Médio incompleto'), ('EMC', 'Ensino Médio completo'), ('ESI', 'Ensino Superior incompleto'), ('ESC', 'Ensino Superior completo')], max_length=50, verbose_name='Escolaridade')),
                ('status_estadocivil', models.CharField(choices=[('SOLTEIRO', 'Solteiro(a)'), ('CASADO', 'Casado(a)'), ('DIVORCIADO', 'Divorciada(a)'), ('VIUVO', 'Viúvo(a)')], max_length=50, verbose_name='Estado Civil')),
                ('profissao', models.CharField(max_length=50, verbose_name='Profissão')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('cep', models.CharField(max_length=14, verbose_name='CEP')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('endereco', models.CharField(max_length=120, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=50, verbose_name='Celular')),
                ('data_cadastro', models.DateField(max_length=50, verbose_name='Data de Cadastro')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'db_table': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Empresa', verbose_name='Empresa')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'vendedores',
                'db_table': 'vendedor',
            },
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'gerentes',
                'db_table': 'gerente',
            },
        ),
    ]
