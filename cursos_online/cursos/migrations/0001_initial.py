# Generated by Django 3.2.6 on 2021-11-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição Simples')),
                ('sobre', models.TextField(blank=True, verbose_name='Sobre o Curso')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de início')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='cursos/imagens', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em ')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['nome'],
            },
        ),
    ]
