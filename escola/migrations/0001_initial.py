# Generated by Django 2.0.7 on 2018-07-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
            },
        ),
    ]
