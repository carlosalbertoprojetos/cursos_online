# Generated by Django 3.2.10 on 2022-02-11 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_rename_anuncios_comentarios_anuncio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('numero', models.IntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('inicio', models.DateField(blank=True, null=True, verbose_name='Início da aula')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='aula', to='cursos.cursos', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['-numero'],
            },
        ),
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('embutido', models.TextField(blank=True, verbose_name='Vídeo da aula')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='aulas/materiais')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='material', to='cursos.aulas', verbose_name='Aulas')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
