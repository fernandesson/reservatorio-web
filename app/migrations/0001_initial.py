# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoEvaporacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=10)),
                ('evaporacao', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historico_evaporacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricoVazoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('vazao', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historico_vazoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservatorio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'reservatorio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParametrosCav',
            fields=[
                ('a', models.FloatField(blank=True, null=True)),
                ('b', models.FloatField(blank=True, null=True)),
                ('c', models.FloatField(blank=True, null=True)),
                ('d', models.FloatField(blank=True, null=True)),
                ('reservatorio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Reservatorio')),
            ],
            options={
                'db_table': 'parametros_cav',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('atual', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('reservatorio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.Reservatorio')),
            ],
            options={
                'db_table': 'volume',
                'managed': False,
            },
        ),
    ]