# Generated by Django 3.1.4 on 2023-06-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_historicoconsumo_historicoemprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicoconsumo',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicoemprestimo',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
