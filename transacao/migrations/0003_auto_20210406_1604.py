# Generated by Django 3.0 on 2021-04-06 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0002_auto_20210405_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtomovimentacao',
            name='movimentacao',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='transacao.Movimentacao', verbose_name='Movimentação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produtomovimentacao',
            name='quantidade',
            field=models.FloatField(default=0, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='data',
            field=models.DateField(auto_now_add=True, max_length=50, verbose_name='Data Movimentação'),
        ),
    ]
