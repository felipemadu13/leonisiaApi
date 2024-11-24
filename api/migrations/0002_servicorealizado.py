# Generated by Django 5.1.3 on 2024-11-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoRealizado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_servico', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
            ],
        ),
    ]