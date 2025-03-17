# Generated by Django 5.1.7 on 2025-03-17 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo_Tarefa', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_croacao', models.DateField(auto_now_add=True)),
                ('data_limite', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('F', 'Finalizada'), ('R', 'Replanejada')], default='P', max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.usuario')),
            ],
        ),
    ]
