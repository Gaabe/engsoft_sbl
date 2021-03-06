# Generated by Django 2.0.7 on 2018-07-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('autor', models.CharField(max_length=200)),
                ('editora', models.CharField(max_length=200)),
                ('edicao', models.CharField(max_length=200, verbose_name='Edição')),
                ('ano_de_publicacao', models.CharField(max_length=200, verbose_name='Ano de publicação')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
