# Generated by Django 5.1.3 on 2024-11-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
