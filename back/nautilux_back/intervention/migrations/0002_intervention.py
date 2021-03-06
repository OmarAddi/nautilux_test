# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-26 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intervention', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('nom_inter', models.CharField(max_length=254)),
                ('lieu', models.CharField(max_length=254)),
                ('date_inter', models.DateField()),
                ('date_crea', models.DateField()),
                ('statut', models.CharField(choices=[('B', 'Brouillon'), ('V', 'Valid\xe9'), ('T', 'Termin\xe9')], max_length=1)),
            ],
        ),
    ]
