# Generated by Django 4.1.3 on 2022-11-23 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_cnhs_2', '0009_alter_candidatos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidatos',
            options={'ordering': ('data_criacao',), 'permissions': [('pode_manipular_cnh', 'pode manipular cnh'), ('pode_manipular_jm', 'pode manipular jm'), ('pode_manipular_crt', 'pode manipular crt'), ('pode_manipular_cedv', 'pode manipular cedv')], 'verbose_name': 'Candidato', 'verbose_name_plural': 'Candidatos'},
        ),
    ]
