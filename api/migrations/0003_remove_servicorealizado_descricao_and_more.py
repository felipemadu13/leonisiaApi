# Generated by Django 5.1.3 on 2024-11-16 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_servicorealizado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicorealizado',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='servicorealizado',
            name='nome_servico',
        ),
        migrations.RemoveField(
            model_name='servicorealizado',
            name='preco',
        ),
        migrations.AddField(
            model_name='servicorealizado',
            name='servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicos_realizados', to='api.servico'),
        ),
    ]