# Generated by Django 3.2.9 on 2021-12-13 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_anuncios_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='updated_at',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='created_at',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='start_date',
            new_name='data_inicial',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='updated_at',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='created_at',
            new_name='criado_em',
        ),
    ]
